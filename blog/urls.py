"""Define URL patterns for blog page."""
from django.urls import path
from django.conf.urls import url
from .views import ModuleDetailView, ModuleListView,  InstructorListView, InstructorDetailView, new_module

from . import views
from .models import *
app_name = 'blog'

urlpatterns = [
    # Home page
    path ('', views.index, name ='index'),
    path ('modules/', views.ModuleListView.as_view(), name = 'modules'),# module display url link
    path ('module/<int:pk>', views.ModuleDetailView.as_view(), name= 'module-detail'), # detail information of the list module
    path ('instructors/', views.InstructorListView.as_view(), name='instructors'),
    path ('instructor/<int:pk>', views.InstructorDetailView.as_view(), name= 'instructor-detail'),
    path ('new_module/', views.new_module, name='new_module'),
    path ('new_instructor/<int:module.pk>/', views.new_instructor, name='new_instructor')
]