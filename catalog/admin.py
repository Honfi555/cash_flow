"""Администрирование моделей каталога."""

from django.contrib import admin
from .models import Status, Type, Category, Subcategory


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    """Администрирование модели Status."""
    list_display = ('name',)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    """Администрирование модели Type."""
    list_display = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Администрирование модели Category."""
    list_display = ('name', 'type')
    list_filter = ('type',)


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    """Администрирование модели Subcategory."""
    list_display = ('name', 'category')
    list_filter = ('category',)
