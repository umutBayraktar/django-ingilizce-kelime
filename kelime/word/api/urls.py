from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter
from .views import WordViewSet

router=DefaultRouter()
router.register('words',WordViewSet,base_name='words')



urlpatterns = [

]
urlpatterns += router.urls

