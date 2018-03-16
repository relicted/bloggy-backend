from django.urls import path
from app.posts import views


app_name = 'posts'

urlpatterns = [
    path('posts/', views.PostList.as_view())
]
