from django.contrib import admin
from django.urls import path, include
from webApp import views

urlpatterns = [
   path('', views.index, name='home'),
   path('login', views.loginUser, name='login'),
   path('logout', views.logoutUser, name='logout'),
   path('totalGDP', views.totalGDP, name='totalGDP'), 
   path('predict', views.predict, name='predict'),
   path('contact', views.contact, name='contact'),
   path('pricing', views.pricing, name='pricing'),
   path('about', views.about, name='about'),
   path('services', views.services, name='services')
]