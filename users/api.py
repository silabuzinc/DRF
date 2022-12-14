from .models import Users
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework import mixins


class UserViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = UserSerializer
    queryset = Users.objects.all()

    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)



class UserViewSetOne(
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = UserSerializer
    queryset = Users.objects.all()
    lookup_field = "username"

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
