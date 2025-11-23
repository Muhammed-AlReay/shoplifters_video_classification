from django.urls import path
from . import views

urlpatterns = [
    path('media/videos', views.upload_video, name='upload_video'),
    path('videos/', views.video_list, name='video_list'),
    path('video/<int:pk>/', views.video_detail, name='video_detail'),
    path('delete/<int:pk>/', views.delete_video, name='delete_video'),
]
