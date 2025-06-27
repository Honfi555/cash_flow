"""URL-маршруты для приложения catalog."""

from django.urls import path
from .views import CatalogListView, add_category, add_status, add_subcategory, add_type

app_name = 'catalog'

urlpatterns = [
    path('', CatalogListView.as_view(), name='list'),
    path('add/category/', add_category, name='add_category'),
    path('add/subcategory/', add_subcategory, name='add_subcategory'),
    path('add/status/', add_status, name='add_status'),
    path('add/type/', add_type, name='add_type'),
]
