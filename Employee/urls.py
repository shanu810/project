from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('emp',views.e1,name='emp'),
    path('elog',views.elogin,name='elog'),
    path('ereg',views.ereg,name='ereg'),
    path('eprofile',views.eprofile,name='eprofile'),
    path('ehome',views.ehome,name='ehome'),
    path('ewaste',views.ewaste,name='ewaste'),
    path('predict<int:id>',views.prediction,name='predict'),
    # path('eresult<int:id>',views.eresult,name='eresult'),
]