from rest_framework import exceptions
from rest_framework import serializers
from rest_framework.authentication import TokenAuthentication

from apps.authentication.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'email', 'nickname', 'is_staff')


class GlobalAuthentication(TokenAuthentication):
    def authenticate(self, request):
        return None


class AuthCustomTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            # Check if user sent email
            """
            if validateEmail(email_or_username):
                user_request = get_object_or_404(
                    User,
                    email=email_or_username,
                )
            """
            #email = user_request.username

            #user = User.objects.get(email=email)
            user = User.login(email=email, password=password)

            if user:
                pass
            else:
                msg = 'Unable to log in with provided credentials.'
                raise exceptions.ValidationError(msg)
        else:
            msg = 'Must include "email or username" and "password"'
            raise exceptions.ValidationError(msg)

        attrs['user'] = user
        return attrs