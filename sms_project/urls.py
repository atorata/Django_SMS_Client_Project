from django.urls import path, include

urlpatterns = [
    path('', include('sms_app.urls')),
]
