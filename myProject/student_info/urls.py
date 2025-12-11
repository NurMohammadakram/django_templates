from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_student/',views.add_student, name='add_student'),
    path('all_student/',views.all_student, name='all_student'),
    path('update_student/<int:id>/',views.update_student, name='update_student'),
]