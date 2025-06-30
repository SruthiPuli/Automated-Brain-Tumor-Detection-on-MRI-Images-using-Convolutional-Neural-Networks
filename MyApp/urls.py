from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Optional: for landing page
    path('upload/', views.tumor_detection_view, name='upload'),  # Fix here
]
