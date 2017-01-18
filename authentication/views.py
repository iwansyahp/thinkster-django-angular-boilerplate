
#from django.shortcuts import render
import json

from django.contrib.auth import authenticate, login, logout

from rest_framework import permissions, viewsets, views, status
from rest_framework.response import Response

from authentication.models import Account
from authentication.permissions import IsAccountOwner
from authentication.serializers import AccountSerializer

class LoginView(views.APIView):
    ''' Tampilan untuk Login User '''
    def post(self, request, format=None):
        ''' Ketika client mensubmit form login '''
        data = json.loads(request.body)

        email = data.get('email', None)
        password = data.get('password', None)

        account = authenticate(email=email, password=password)

        if account is not None:
            if account.is_active:
                login(request, account)

                serialized = AccountSerializer(account)

                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled'
                }, status=status.HTTP_401_UNAUTHORIZED)

        # akun tidak ditemukan
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid'
            }, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(views.APIView):
    ''' View untuk logout pengguna '''
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, format=None):
        ''' Pengguna melakukan logout'''
        logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)


# Create your views here.
class AccountViewSet(viewsets.ModelViewSet):
    '''' Class yang akan membangkitkan view CRUD untuk Account '''
    # viewsets >> as the name implies, is a set of views. Specifically,
    # the ModelViewSet offers an interface for listing, creating, retrieving, updating
    # and destroying objects of a given model.
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        ''' Memperoleh permission yang sesuai dengan jenis Account'''
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        '''Membuat user yang sudah di serialisasi'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            Account.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message':'Account could not be created with received data'
        }, status=status.HTTP_400_BAD_REQUEST)
