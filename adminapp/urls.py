from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('ahome',views.ahome,name='ahome'),
    path('areg',views.areg,name='areg'),
    path('alogin',views.alogin,name='alogin'),
    path('tables',views.tables,name='tables'),
    # path('ehome',views.ehome,name='ehome'),
    # path('ewaste',views.ewaste,name='ewaste'),
    # path('predict<int:id>',views.prediction,name='predict'),
    # path('eresult<int:id>',views.eresult,name='eresult'),
]