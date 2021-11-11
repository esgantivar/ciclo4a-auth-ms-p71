import datetime
import jwt
from django.http import JsonResponse
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.views import APIView

from auth_app.models import Usuario
from auth_ms.settings import SECRET_KEY


class CustomSerializer(serializers.Serializer):
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label="Token",
        read_only=True
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        if username and password:
            user: Usuario = Usuario.objects.get(username=username)
            if not user.check_password(password):
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs


class ManualLoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('usuario')
        password = request.data.get('contrasena')
        try:
            user = Usuario.objects.get(username=username)
            if user.check_password(password):
                now = datetime.datetime.now()
                access_token = jwt.encode(
                    payload={
                        'exp': now + datetime.timedelta(hours=1),
                        'user_id': user.id,
                        'username': user.username,
                        'email': user.email
                    },
                    key=SECRET_KEY
                )
                return Response({
                    'access_token': access_token
                })
            else:
                return Response({
                    'error': f'Credenciales invalidas'
                }, status=status.HTTP_400_BAD_REQUEST)
        except Usuario.DoesNotExist:
            return Response({
                'error': f'Usuario: {username} no existe'
            }, status=status.HTTP_400_BAD_REQUEST)


class LoginCustomView(APIView):
    serializer_class = CustomSerializer

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context={'request': request})
        if login_serializer.is_valid(raise_exception=True):
            user = login_serializer.validated_data['user']
            now = datetime.datetime.now()
            access_token = jwt.encode(
                payload={
                    'exp': now + datetime.timedelta(hours=1),
                    'user_id': user.id,
                    'username': user.username,
                    'email': user.email
                },
                key=SECRET_KEY
            )
            return Response({
                'access_token': access_token
            })
        else:
            return Response({
                'error': 'credenciales no existen o son invalidas'
            }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data,
                                                 context={'request': request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            now = datetime.datetime.now()
            access_token = jwt.encode(
                payload={
                    'exp': now + datetime.timedelta(hours=1),
                    'user_id': user.id
                },
                key=SECRET_KEY
            )
            return Response({
                'access_token': access_token
            })
        else:
            return Response({
                'error': 'credenciales no existen o son invalidas'
            }, status=status.HTTP_400_BAD_REQUEST)


class AuthView(APIView):
    user: Usuario

    def dispatch(self, request, *args, **kwargs):
        try:
            if not request.headers.get('Authorization'):
                raise Exception('No token')
            token = request.headers.get('Authorization').split('Bearer ')[1]
            decoded = jwt.decode(token, key=SECRET_KEY, algorithms=['HS256'])
            self.user = Usuario.objects.get(id=decoded.get('user_id'))
            if self.user.is_active:
                return super(AuthView, self).dispatch(request, *args, **kwargs)
            else:
                return JsonResponse({'error': 'El Usuario no esta activo'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return JsonResponse({'error': e.__str__()}, status=status.HTTP_401_UNAUTHORIZED)


class CheckToken(AuthView):
    def get(self, request, **kwargs):
        return Response({
            'status': 'ok'
        })


class Usuarios(AuthView):
    def get(self, request, **kwargs):
        return Response({
            'status': 'ok'
        })