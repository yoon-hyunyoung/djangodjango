from . import views
from django.urls import path, include
from rest_framework import routers
from yoonproject import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('epl/', views.EPLView, name='epl'),
    path('efl/', views.EFLView, name='efl'),
    path('league1/', views.LEAGUE1View, name='league1'),
    path('bigmatch/', views.BigmatchView, name='bigmatch'),
    path('bigmatch/<int:seq>', views.BigmatchdeleteView, name='bigmatch_d'),
    path('league1/<int:seq>', views.LEAGUE1deleteView, name='league1_d'),
    path('epl/<int:seq>', views.EPLdeleteView, name='epl_d'),
    path('efl/<int:seq>', views.EFLdeleteView, name='efl_d'),
    path('eplgroup/', views.EPLGroupView, name='eplgroup'),
    path('eplallselectview/', views.EPLAllSelectView, name='eplallselectview'),
    path('eplallselectview/<int:seq>', views.EPLAllSelectDeleteView, name='eplallselectview_d'),
    
    
    
    ]
