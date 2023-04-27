from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home',views.s1,name='home'),
    path('slog',views.slogin,name='slog'),
    path('sreg',views.sreg,name='sreg'),
    path('profile',views.profile,name='profile'),
    path('shome',views.shome,name='shome'),
    path('image',views.image,name='image'),
    path('viewimg',views.viewimg,name='viewimg'),
    path('payment<int:pid>',views.payment,name='payment'),
    
]