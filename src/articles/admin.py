from django.contrib import admin

# Register your models here.
from .models import Article, Comments

admin.site.register(Article)
admin.site.register(Comments)