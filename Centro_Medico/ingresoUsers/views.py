from django.views import View
from .models import Users
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.response import Response


# vista basada en la clase 
# metodo para listar los usuarios //para probar si sirve
@api_view(['GET'])
def listaUsers(request):
    usuarios = Users.objects.all()
    serializer = UserSerializer(usuarios, many=True)
    return Response(serializer.data)

# metodo para agregar usuarios
@api_view(['POST'])  
def ingresoUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)
    
# metodo para eliminar usuarios
@api_view(['DELETE'])
def eliminarUser(request, pk):
    usuarios = Users.objects.get(id=pk)
    usuarios.delete()
    return Response('Usuario eliminado')