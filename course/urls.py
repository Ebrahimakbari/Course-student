from django.urls import path
from . import views

urlpatterns = [
    path('', views.TestClass.as_view(), name='dashboard')
]
