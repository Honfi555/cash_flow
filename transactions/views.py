"""Представления для работы с транзакциями."""

from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import TransactionForm
from .models import Transaction
from catalog.models import Category, Subcategory, Status, Type


class TransactionListView(ListView):
    """Отображает список транзакций с возможностью фильтрации."""
    model = Transaction
    template_name = 'transactions/list.html'
    context_object_name = 'transactions'
    paginate_by = 20

    def get_queryset(self):
        """Возвращает отфильтрованный список транзакций по параметрам запроса."""
        queryset = super().get_queryset()

        # Фильтрация по дате (период)
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        if start_date:
            queryset = queryset.filter(date__gte=start_date)
        if end_date:
            queryset = queryset.filter(date__lte=end_date)

        # Фильтрация по статусу
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status_id=status)

        # Фильтрация по типу
        transaction_type = self.request.GET.get('type')
        if transaction_type:
            queryset = queryset.filter(type_id=transaction_type)

        # Фильтрация по категории
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category_id=category)

        # Фильтрация по подкатегории
        subcategory = self.request.GET.get('subcategory')
        if subcategory:
            queryset = queryset.filter(subcategory_id=subcategory)

        return queryset

    def get_context_data(self, **kwargs):
        """Добавляет в контекст списки статусов, типов, категорий и подкатегорий для фильтров."""
        context = super().get_context_data(**kwargs)

        # Заполняем контекст для фильтров
        context['statuses'] = Status.objects.all()
        context['types'] = Type.objects.all()
        context['categories'] = Category.objects.all()
        context['subcategories'] = Subcategory.objects.all()

        return context


class TransactionCreateView(LoginRequiredMixin, CreateView):
    """Создаёт новую транзакцию."""
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/form.html'
    success_url = reverse_lazy('transactions:list')


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирует существующую транзакцию."""
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/form.html'
    success_url = reverse_lazy('transactions:list')


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    """Удаляет транзакцию после подтверждения."""
    model = Transaction
    template_name = 'transactions/confirm_delete.html'
    success_url = reverse_lazy('transactions:list')


def load_categories(request):
    """Возвращает JSON-список категорий для заданного type_id (AJAX-запрос)."""
    type_id = request.GET.get('type_id')
    categories = Category.objects.filter(type_id=type_id).order_by('name')
    data = [{'id': cat.id, 'name': cat.name} for cat in categories]
    return JsonResponse(data, safe=False)


def load_subcategories(request):
    """Возвращает JSON-список подкатегорий для заданного category_id (AJAX-запрос)."""
    category_id = request.GET.get('category_id')
    subcategories = Subcategory.objects.filter(category_id=category_id).order_by('name')
    data = [{'id': sub.id, 'name': sub.name} for sub in subcategories]
    return JsonResponse(data, safe=False)
