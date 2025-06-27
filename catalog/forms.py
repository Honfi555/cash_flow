"""Формы для работы с моделями каталога."""

from django import forms
from .models import Category, Subcategory, Status, Type


class CategoryForm(forms.ModelForm):
    """Форма для модели Category."""
    class Meta:
        model = Category
        fields = ['type', 'name']


class SubcategoryForm(forms.ModelForm):
    """Форма для модели Subcategory."""
    class Meta:
        model = Subcategory
        fields = ['category', 'name']


class StatusForm(forms.ModelForm):
    """Форма для модели Status."""
    class Meta:
        model = Status
        fields = ['name']


class TypeForm(forms.ModelForm):
    """Форма для модели Type."""
    class Meta:
        model = Type
        fields = ['name']
