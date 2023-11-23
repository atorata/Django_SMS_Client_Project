from django.urls import path

from . import views

urlpatterns = [
    path('send_sms/', views.send_sms, name='send_sms'),
    path('login/', views.login_view, name='login'),
    path('', views.send_sms, name='send_sms'),
]