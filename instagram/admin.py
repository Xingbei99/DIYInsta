# Administrator for the django application.

from django.contrib import admin
from instagram.models import User, Post

# Register your models here.
admin.site.register(User)
admin.site.register(Post)
