from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('wast',views.w1,name='wast'),
    path('wlog',views.wlogin,name='wlog'),
    path('wreg',views.wreg,name='wreg'),
    path('wprofile',views.wprofile,name='wprofile'),
    path('whome',views.whome,name='whome'),
    path('image<int:id>',views.image,name='image'),
    # path('selemp<int:id>',views.selemp,name='selemp'),
    path('vimg',views.vimg,name='vimg'),
]