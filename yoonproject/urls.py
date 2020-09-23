from . import views
from django.urls import path, include

urlpatterns = [
    path('epl/', views.EPLView, name='EPL')
]

