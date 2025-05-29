from django.urls import path
from . import views

urlpatterns = [
    
    path('project/<int:project_id>/bid/', views.bid_project, name='bid_project'),
]