# Microservicio Autenticación

## Tareas a  resolver

1. Manejo de los usuarios
2. Autenticación via JWT

### Usuarios

1. Crear el modelo
2. agregar paquete de pip install djangorestframework
3. Serializadores
4. Vistas
5. Agregar las urls


### Usuarios (2)
1. Crear la vista
2. Agregar las urls


### Autenticación via JWT [Manual]
1. Instalar la dependencia que nos permite trabajar con JWT `$ pip install PyJWT`
2. Crear la vista para realizar la autenticación
3. Agregar la url

### Verificación de identidad via JWT [Manual]
1. Crear la vista para verificar la identidad
2. Agregar la url

### Autenticación via JWT 
1. Instalar la dependencia `$ pip install djangorestframework-simplejwt`
2. Agregar la url de autenticación que se encuentra disponible en el paquete `rest_framework_simplejwt.views`
   1. TokenObtainPairView
   2. TokenRefreshView
3. Crear la vista para verificar el token