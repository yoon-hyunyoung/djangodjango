from django.urls import path, include
from . import views
urlpatterns = [
    path('students/', views.StudentView),
    path('students/<int:id>', views.StudentDetailView),
    path('scores/', views.ScoreView),
    
]