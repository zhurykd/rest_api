from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics, status
from rest_framework.authtoken.models import Token
from core.serializers import UserSerializer, AuthTokenSerializer
from rest_framework import parsers, renderers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

User = get_user_model()


class AuthTokenView(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    queryset = User.objects.all()
    serializers = AuthTokenSerializer

    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        a = Token.objects.filter(user=user)
        if a.exists():
            a.delete()
        token = Token.objects.create(user=user)

        return Response({'token': token.key})


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    _token = None

    def perform_create(self, serializer):
        serializer.save()
        AuthTokenSerializer(data=serializer.data)
        self._token = Token.objects.create(user=serializer.instance)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = dict()
        data.update({'token': self._token.key})
        data.update(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)