from django.urls import path
from . import views

urlpatterns = [
    path('', views.TestClass.as_view(), name='dashboard'),
    path('profile/', views.StudentProfileView.as_view(), name='student_profile'),
    path('profile/edit/', views.StudentProfileEditView.as_view(), name='student_profile_edit'),
]
