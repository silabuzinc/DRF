from . import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'todo', api.TodoViewSet, 'todos')

api_urlpatterns = router.urls