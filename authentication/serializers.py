from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from authentication.models import Account

class AccountSerializer(serializers.ModelSerializer):
    '''Menseriali Account, karena digunakan untuk otentikasi user'''
    #write-only: memastikan client tidak dapat melihat isi file
    password = serializers.CharField(write_only=True, required=False)

    confirm_password = serializers.CharField(write_only=True,
                                             required=False)

    # pelajari tentang class Meta di Python (like private class)
    class Meta:
        ''' Metada untuk Account yang akan digunakan '''
        model = Account #karena class (super) ini adalah Serializer untuk model
        fields = ('id', 'email', 'username',
                  'created_at', 'updated_at',
                  'first_name', 'last_name',
                  'tagline', 'password', 'confirm_password',)

        # fields superuser tidak boleh dimasukkan

        # read-only karena fields berikut auto-gen
        read_only_fields = ('created_at', 'updated_at',)

        # deserialization JSON >> Python object
        def create(self, validated_data):
            '''Membuat user baru'''
            return Account.objects.create(**validated_data)

        # deserialization JSON >> Python object
        def update(self, instance, validated_data):
            '''Memperbarui data yang ada'''
            # pada tut, bukan validated_data.get() tapi attrs.get()
            instance.username = validated_data.get('username', instance.username)
            instance.tagline = validated_data.get('tagline', instance.tagline)

            instance.save()

            password = validated_data.get('password', None)
            confirm_password = validated_data.get('confirm_password', None)

            if password and confirm_password and password == confirm_password:
                instance.set_password(password)
                instance.save()

            #{info} This is a naive implementation of
            # how to validate a password. I would not recommend
            # using this in a real-world system, but for our purposes
            # this does nicely.
            update_session_auth_hash(self.context.get('request'), instance)

            return instance
