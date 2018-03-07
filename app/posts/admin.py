from django.contrib import admin

from app.accounts.models import User
from app.posts.models import Post

# Register your models here.
admin.site.register(Post)
