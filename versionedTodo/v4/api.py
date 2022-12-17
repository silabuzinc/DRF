from todos.models import Todo
from .serializers import TodoV4Serializer
from rest_framework import status
from rest_framework.response import Response
from .pagination import StandardResultsSetPagination
from rest_framework import viewsets, filters 
from rest_framework.permissions import IsAuthenticated
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoV4Serializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    permission_classes = [IsAuthenticated]

    search_fields = ['author__id']
    ordering = ('-id')
    throttle_scope = 'get'