from django.contrib import admin
from .models import Post
# Register your models here.

# chaanging what needs to be displayed on the admin page for the Post
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "body",
    )
admin.site.register(Post, PostAdmin)