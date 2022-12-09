from rest_framework import routers
from .api import TodoViewSet

router = routers.DefaultRouter()

router.register('api/v1/todo', TodoViewSet, 'todos')

urlpatterns = router.urls