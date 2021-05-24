from django.contrib import admin

# Register your models here.
from .models import Article


# Admin Panel

@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_filter = ('title', 'description')
    list_display = ('title',)
    # ordering = ('createdAt',)
