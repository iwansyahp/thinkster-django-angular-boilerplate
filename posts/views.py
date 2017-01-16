from django.shortcuts import render

from rest_framework import permissions, viewsets
from rest_framework.response import Response

from posts.models import Post
from posts.serializers import PostSerializer
from posts.permissions import IsAuthorOfPost


# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    '''Menampilkan Postingan yang tersimpan'''
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer

    def get_permissions(self):
        '''Dapatkan izin untuk....'''
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAuthorOfPost(),)
    
def perform_create(self, serializer):
    ''' Membuat tulisan baru '''
    instance = serializer.save(author=self.request.user)

    return super(PostViewSet, self).perform_create(serializer)

class AccountPostViewSet(viewsets.ViewSet):
    ''' Class untuk menampilkan seluruh tulisan '''
    queryset = Post.objects.select_related('author').all()
    serializer_class = PostSerializer

    def list(self, request, account_username=None):
        '''Daftarkan seluruh tulisan'''
        queryset = serlf.queryset.filter(author_username=account_username)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)
