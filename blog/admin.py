from django.contrib import admin
from .models import Post, Comment, Tag, Photo

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Photo)
