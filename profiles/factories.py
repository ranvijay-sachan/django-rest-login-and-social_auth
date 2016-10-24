from profiles.serializers.social_auth_serializers import SocialAuthSerializer
from profiles.serializers.auth_serializers import AuthTokenSerializer
from profiles.utils.backend import BackendType


class AuthenticationSerializerFactory(object):
    @staticmethod
    def get_authentication_serializer(backend, data, request):
        if int(backend) not in list(map(int, BackendType)):
            raise ValueError('Allowed backends types: ', list(map(int, BackendType)))
        return {
            BackendType.AUTH: AuthTokenSerializer(data=data, context={'request': request}),
            BackendType.FACEBOOK: SocialAuthSerializer(data=data, context={'request': request, 'backend': backend}),
            BackendType.GOOGLE: SocialAuthSerializer(data=data, context={'request': request, 'backend': backend}),
        }[int(backend)]