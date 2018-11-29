from django.urls import path
from .views import AddData,DataSubmit

urlpatterns = [
    path('add',AddData),
    path('DataSubmit',DataSubmit)
]