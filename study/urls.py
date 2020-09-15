from django.urls import path, include
from . import views
urlpatterns = [
    # path('students/', views.StudentView),
    # path('students/<int:id>', views.StudentDetailView),
    # path('scores/', views.ScoreView),
    # path('scores/<int:id>', views.ScoreDetailView),
    path('students/', views.StudentView.as_view()),
    path('students/<pk>', views.StudentDetailView.as_view()),
    path('scores/', views.ScoreView.as_view()),
    path('scores/<pk>', views.ScoreDetailView.as_view())
]