from rest_framework import routers
from .api import TodoViewSet, DeleteAllTodo, GetAllTodo, Get2Todo
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()

router.register('api/v1/todo', TodoViewSet, 'todos')

urlpatterns = [
    path('api/v1/todo/delAll', DeleteAllTodo.as_view(),name='delAll'),  
    path('api/v1/todo/getAll', GetAllTodo.as_view(),name='getAllTodo'),
    # Simple JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Tarea
    path('api/v1/todo/get2', Get2Todo.as_view(),name='get2Todo'),
]

urlpatterns += router.urls