"""URL-маршруты для приложения transactions."""

from django.urls import path

from .views import (
	TransactionListView,
	TransactionCreateView,
	TransactionUpdateView,
	TransactionDeleteView,
	load_categories,
	load_subcategories
)

app_name = 'transactions'

urlpatterns = [
	path('', TransactionListView.as_view(), name='list'),
	path('add/', TransactionCreateView.as_view(), name='add'),
	path('<int:pk>/edit/', TransactionUpdateView.as_view(), name='edit'),
	path('<int:pk>/delete/', TransactionDeleteView.as_view(), name='delete'),
	path('ajax/load-categories/', load_categories, name='ajax_load_categories'),
	path('ajax/load-subcategories/', load_subcategories, name='ajax_load_subcategories'),
]
