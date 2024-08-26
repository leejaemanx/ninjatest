from django.urls import path
from devices.api import app

urlpatterns = [
  path('', app.urls)
]