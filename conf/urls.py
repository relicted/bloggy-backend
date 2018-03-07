from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as drf_views


urlpatterns = [
    path('admin', admin.site.urls),
    path('auth/', drf_views.obtain_auth_token, name='auth'),
    path('accounts/', include('app.accounts.urls', namespace='accounts')),
    path('posts/', include('app.posts.urls', namespace='posts'))
]
