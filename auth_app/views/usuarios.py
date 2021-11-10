from django.shortcuts import render

from auth_app.models import Usuario
from auth_app.serializers import UsuarioSerializer
from rest_framework import views, status
from rest_framework.response import Response

# Create your views here.

'''
    Crear usuarios
'''


class CrearUsuarioView(views.APIView):

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

