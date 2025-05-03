from django.contrib import admin
from .models import  Category, Product, Cart, NewsCategory, News


# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)
    ordering = ('-created_at',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('category', 'created_at')
    ordering = ('-created_at',)