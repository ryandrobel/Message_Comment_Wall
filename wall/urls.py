from django.urls import path    
from . import views

urlpatterns = [
    path('', views.wall),
    path('message', views.post_message),
    path('comment/<int:post_id>', views.post_comment)
]