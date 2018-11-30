from django.urls import path,include
from rest_framework import serializers,routers,viewsets
from users.models import UserData

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ('first_name','last_name','url')

class SingleUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ('__all__')

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserSerializers

class SingleUserViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = SingleUserSerializers

router = routers.DefaultRouter()
router.register(r'',UserViewSet)
router.register(r'Details',SingleUserViewSet)

urlpatterns = [
    path('',include(router.urls)),
]