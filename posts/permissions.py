from rest_framework import permissions

class IsAuthorOfPost(permissions.BasePermission):
    ''' Class untuk melihat client yang mengakses '''
    def has_object_permission(self, request, view, post):
        ''' Apakah client yang mengakses adalah penulis dari post '''
        if request.user:
            return post.author == request.user
        return False
        