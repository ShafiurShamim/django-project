from django.contrib import admin
from blog.models import Post


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_created')


admin.site.register(Post, BlogAdmin)
