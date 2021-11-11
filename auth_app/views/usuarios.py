from rest_framework import views, status, generics
from rest_framework.response import Response

from auth_app.models import Usuario
from auth_app.serializers import UsuarioSerializer

'''
    Crear usuarios
'''


class CrearUsuarioView(views.APIView):
    def get(self, request, *args, **kwargs):
        usuarios = Usuario.objects.filter()
        tmp = []
        for u in usuarios:
            tmp.append(UsuarioSerializer(u).data)
        return Response({
            'usuarios': tmp
        })

    def post(self, request, *args, **kwargs):
        serializer = UsuarioSerializer(data=request.data)
        valid = serializer.is_valid()
        if valid:
            serializer.save()
            return Response({}, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'error': 'mensaje'
            }, status=400)


class DetalleUsuarioView(generics.RetrieveUpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

