from django.urls import path
from app.posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.Posts.as_view()),
    path('<int:pk>', views.Detail.as_view())

]
