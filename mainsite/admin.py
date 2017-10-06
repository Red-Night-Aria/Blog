from django.contrib import admin
from .models import Post, Pastime, Tag
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

admin.site.register(Post, PostAdmin)
admin.site.register(Pastime)
admin.site.register(Tag)