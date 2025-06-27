"""Представления для приложения catalog."""

from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import CategoryForm, StatusForm, SubcategoryForm, TypeForm
from .models import Category, Status, Type


class CatalogListView(TemplateView):
    """Отображает список каталога с фильтрами."""
    template_name = 'catalog/list.html'

    def get_context_data(self, **kwargs):
        """Добавляет данные для фильтров и списка типов."""
        ctx = super().get_context_data(**kwargs)
        ctx['statuses'] = Status.objects.all().order_by('name')
        ctx['types'] = Type.objects.prefetch_related('categories__subcategories').all().order_by('name')
        return ctx


def add_category(request):
    """Обрабатывает создание новой категории."""
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog:list')
    else:
        form = CategoryForm()

    types = Type.objects.all()

    return render(request, 'catalog/add_category.html', {'form': form, 'types': types})


def add_subcategory(request):
    """Обрабатывает создание новой подкатегории."""
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog:list')  # перенаправляем на страницу с подкатегориями
    else:
        form = SubcategoryForm()

    # Получаем все категории для отображения в выпадающем списке
    categories = Category.objects.all()

    return render(request, 'catalog/add_subcategory.html', {'form': form, 'categories': categories})


def add_status(request):
    """Обрабатывает создание нового статуса."""
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog:list')
    else:
        form = StatusForm()
    return render(request, 'catalog/add_status.html', {'form': form})


def add_type(request):
    """Обрабатывает создание нового типа."""
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog:list')
    else:
        form = TypeForm()
    return render(request, 'catalog/add_type.html', {'form': form})
