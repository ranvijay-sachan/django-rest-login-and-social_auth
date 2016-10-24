import logging

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.parsers import FormParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .factories import AuthenticationSerializerFactory

logger = logging.getLogger(__name__)


class LoginView(APIView):
    """
    Authenticates a user according to the authentication backend
    and return token in the response.
    """
    parser_classes = (FormParser, JSONParser)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def post(self, request, backend, format=None):
        try:
            data = request.data
            if backend is not None:
                serializer = AuthenticationSerializerFactory.get_authentication_serializer(
                    backend, data, request)
                if serializer.is_valid():
                    return Response(serializer.validated_data, status=status.HTTP_200_OK)
                logger.error(str(serializer.errors))
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"backend": ["Authentication backend is required"]}, status=status.HTTP_400_BAD_REQUEST)
        except BaseException as e:
            logger.error(str(e.message))
            return Response(e.message, status=status.HTTP_400_BAD_REQUEST)
