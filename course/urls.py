from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('profile/', views.StudentProfileView.as_view(), name='student_profile'),
    path('profile/edit/', views.StudentProfileEditView.as_view(), name='student_profile_edit'),
    path('course-selection/', views.course_selection_view, name='course_selection'),
    path('get-department-courses/', views.get_department_courses, name='get_department_courses'),
    path('enroll-course/', views.enroll_course, name='enroll_course'),
]
