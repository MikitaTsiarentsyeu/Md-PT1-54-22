import logging
from turtle import home
from django.urls import path
from.import views 
urlpatterns = [
    path('', views.lilo,name='home'),

    path('otzyv/', views.test,name= 'otzyv'),

    path('zayavka/', views.test1,name='zayavka'),

    path('Soc.seti/', views.index,name='Soc.seti'),



    path('register/', views.register,name='register'),
    path('login/', views.login,name='login'),





    
]
