from rest_framework import views, status, generics
from rest_framework.response import Response

from auth_app.models import Usuario
from auth_app.serializers import UsuarioSerializer


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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'error': 'mensaje'
            }, status=400)


class DetalleUsuarioView(generics.RetrieveUpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    '''
        def partial_update(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = self.serializer_class(instance, data={
                'first_name': 'Juan',
                'last_name': 'fasdf'
            })
            for user in self.queryset.filter():
                user.set_password('123')
                user.save()
    
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=HTTP_200_OK)
            return Response(data="wrong parameters", status=HTTP_400_BAD_REQUEST)
    '''
