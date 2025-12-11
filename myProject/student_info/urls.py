from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/add_student', views.add_student, name='add student'),
    path('/all_student', views.add_student, name='all student')
]