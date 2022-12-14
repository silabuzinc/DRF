from rest_framework import routers
from .api import UserViewSet, UserViewSetOne
from django.urls import path
from .routers import CustomRouter

router = CustomRouter()

router.register('', UserViewSet, 'users')
router.register('', UserViewSetOne, 'oneUser')

urlpatterns = router.urls
