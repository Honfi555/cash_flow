"""Формы для работы с транзакциями."""

from django import forms
from .models import Transaction
from catalog.models import Category, Subcategory


class TransactionForm(forms.ModelForm):
    """Форма для создания и редактирования транзакций."""
    class Meta:
        model = Transaction
        fields = ['date', 'status', 'type', 'category', 'subcategory', 'amount', 'comment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        """Инициализирует форму и настраивает queryset для полей категории и подкатегории."""
        super().__init__(*args, **kwargs)

        # Чтобы подкатегория была доступна только после выбора категории
        if 'category' in self.data:
            try:
                cat_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=cat_id)
            except (ValueError, TypeError):
                self.fields['subcategory'].queryset = Subcategory.objects.none()
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategories
        else:
            self.fields['subcategory'].queryset = Subcategory.objects.none()

        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['category'].queryset = Category.objects.filter(type_id=type_id)
            except (ValueError, TypeError):
                self.fields['category'].queryset = Category.objects.none()
        elif self.instance.pk:
            self.fields['category'].queryset = self.instance.type.categories
        else:
            self.fields['category'].queryset = Category.objects.none()
