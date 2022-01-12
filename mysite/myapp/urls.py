from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.index, name='index'),
    path('otp/', views.otp_login, name='otp'),
]
