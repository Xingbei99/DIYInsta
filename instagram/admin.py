# Administrator for the django application.

from django.contrib import admin
from instagram.models import Post

# Register your models here.
admin.site.register(Post)
