from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.authtoken import views as drf_views
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('auth/', drf_views.obtain_auth_token, name='auth'),
    path('', include('app.accounts.urls')),
    path('', include('app.friendship.urls')),
    path('', include('app.posts.urls', namespace='posts')),
    path('', include_docs_urls(title='Bloggy API'))

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]
