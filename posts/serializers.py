from rest_framework import serializers
from authentication.serializers import AccountSerializer
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    ''' Pe-serial post pengguna '''
    author = AccountSerializer(read_only=True, required=False)

    class Meta:
        ''' Meta-data dari model yang akan diserialkan '''
        model = Post

        fields = ('id', 'author', 'content', 'created_at', 'updated_at',)
        read_only_fields = ('id', 'created_at', 'updated_at')
    
    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(PostSerializer, self).get_validation_exclusions()

        return exclusions + ['author']
