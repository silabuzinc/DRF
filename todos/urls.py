from rest_framework import routers
from .api import TodoViewSet, DeleteAllTodo, GetAllTodo, Get2Todo,AllTodo, OneTodo, TodoViewSetCustom
from django.urls import path, re_path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from versionedTodo.v3.router import api_urlpatterns as api_v3
from versionedTodo.v4.router import api_urlpatterns as api_v4

router = routers.DefaultRouter()

urlpatterns = [
    path('api/v1/todo/delAll', DeleteAllTodo.as_view(),name='delAll'),  
    path('api/v1/todo/getAll', GetAllTodo.as_view(),name='getAllTodo'),
    # Simple JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Tarea
    path('api/v1/todo/get2', Get2Todo.as_view(),name='get2Todo'),
    path('api/v2/todo/', AllTodo.as_view(), name = 'fullView'),
    path('api/v2/todo/<int:pk>', OneTodo.as_view(), name = 'OneTodo'),
    re_path(r'^api/v3/', include(api_v3)),
    re_path(r'^api/v4/', include(api_v4)),
]

urlpatterns += router.urls