from . import views
from django.urls import path, include
from rest_framework import routers
from yoonproject import views


urlpatterns = [
    path('epl/', views.EPLView, name='epl'),
    path('efl/', views.EFLView, name='efl'),
    path('league1/', views.LEAGUE1View, name='league1'),
    path('bigmatch/', views.BigmatchView, name='bigmatch'),
    path('bigmatch/<int:seq>', views.BigmatchdeleteView, name='bigmatch_d'),
    path('league1/<int:seq>', views.LEAGUE1deleteView, name='league1_d'),
]
