from .models import Todo
from rest_framework import viewsets
from .serializers import TodoSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer


class DeleteAllTodo(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request):
        # Elimina todos los registros
        Todo.objects.all().delete()
        # Retorna un status code de 204 indicando que no existe contenido dentro de nuestra base de datos
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetAllTodo(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)


# Tarea
class Get2Todo(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        todos = Todo.objects.all()[:2]
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)





    
