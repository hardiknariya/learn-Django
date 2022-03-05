from django.core.serializers import serialize
import json
from account import models
from rest_framework.authtoken.models import Token


class UserSerializer(object):
    """
    This class provide helper methods for user related serializers.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = self.context['request']
        self.user = None

    def get_data(self):
        """
               Serialize user and its related objects.
               A serializer must provide self.user to consume this method
               """
        user = serialize('json', [self.user])
        user = json.loads(user)[0]['fields']
        user.pop('password')
        user.pop('groups')
        user.pop('is_superuser')
        user.pop('is_staff')
        # user.pop('is_active')
        user.pop('user_permissions')
        user.pop('last_login')
        user.pop('date_joined')

        user['token'] = self.user.auth_token.key
        user['id'] = self.user.id

        # if self.user.photo:
        #     user['photo'] = self.request.build_absolute_uri(self.user.photo.url)

        return user

    def generate_auth_token(self):
        token, _ = Token.objects.get_or_create(user=self.user)

        # if token:
        #     # If the token is expired then delete and generate a new one.
        #     token.delete()
        #     Token.objects.create(user=self.user)
