from django.contrib import admin
from djangotest.kore.models import Post

# Register your models here.
admin.site.register(Post, admin.ModelAdmin)
