from django.utils.translation import ugettext_lazy as _

from rest_framework import exceptions, serializers
from social.apps.django_app.utils import psa
from social.apps.django_app.utils import load_strategy, load_backend

from profiles.models import User
from profiles.serializers.profile_serializers import BaseUserSerializer

from profiles.utils.backend import AuthBackend


class SocialAuthSerializer(serializers.Serializer):
    accessToken = serializers.CharField()

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        access_token = attrs.get('accessToken')
        backend = self.context['backend']

        if access_token:
            user = register_by_access_token(self.context['request'], AuthBackend.get_backend_text(backend))

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise exceptions.ValidationError(msg)
            else:
                msg = _('Unable to log in with provided credentials.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Must include "accessToken" and "backend".')
            raise exceptions.ValidationError(msg)

        data = dict()
        data['user'] = BaseUserSerializer(user).data
        data['token'] = user.auth_token.key

        return data


@psa()
def register_by_access_token(request, backend):
    uri = ''

    strategy = load_strategy(request)
    backend = load_backend(strategy, backend, uri)  # Split by spaces and get the array
    if request.data['accessToken'] is None:
        msg = 'No access token provided.'
        return msg
    else:
        access_token = request.data['accessToken']

    # Real authentication takes place here
    user = backend.do_auth(access_token)

    return user
