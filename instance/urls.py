from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('instance/<int:pk>/', views.instanceView, name='instance'),
    path('instance-create/', views.instanceCreate, name='instance-create'),
    path('instance-update/<int:pk>/', views.instanceUpdate, name='instance-update'),
    path('article/<int:pk>/', views.articleView, name='article'),
    path('article-create/', views.articleCreate, name='article-create'),
    path('article-update/<int:pk>/', views.articleUpdate, name='article-update'),
    path('article-list/', views.articleList, name='article-list'),
    path('instance-list/', views.instanceList, name='instance-list'),
    path('instance-delete/<int:pk>/', views.instanceDelete, name='instance-delete'),
    path('article-delete/<int:pk>/', views.articleDelete, name='article-delete'),
    path('instance/<int:pk>/download/', views.instanceDownload, name='instance-download'),
]