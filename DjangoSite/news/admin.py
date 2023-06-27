from django.contrib import admin

from news.models import Category, Article

admin.site.register(Category)
admin.site.register(Article)
