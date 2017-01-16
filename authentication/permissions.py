from rest_framework import permissions

class IsAccountOwner(permissions.BasePermission):
    ''' Memeriksa pemilik akun yang aktif pada sesi'''
    # apakah user sekarang (account) sama dengan yang membuat request
    def has_object_permission(self, request, view, account):
        '''Memeriksa apakah user yang me-request sama dengan user yang memiliki akun ini'''
        if request.user:
            return account == request.user
        return False
