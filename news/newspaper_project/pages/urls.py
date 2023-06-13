from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]

#http://127.0.0.1:8000/users/password_change/  
