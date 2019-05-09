from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class MyObtainAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        perfil = user.perfil
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


my_obtain_auth_token = MyObtainAuthToken.as_view()
