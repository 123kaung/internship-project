from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('post/', views.post_project, name='post_project'),
]