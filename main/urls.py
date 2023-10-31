from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.main, name='main'),
    path('posts/<int:post_id>/', views.post, name='post')
]
