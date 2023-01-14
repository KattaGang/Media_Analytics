from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('signup/', views.loginUser, name='register'),
    path('logout/', views.logoutUser, name='logout'),
]