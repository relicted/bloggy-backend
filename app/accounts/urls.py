from django.urls import path
from app.accounts import views


app_name = 'accounts'

urlpatterns = [
    path('', views.UsersList.as_view(), name='users')

]