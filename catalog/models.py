"""Модели каталога: Status, Type, Category и Subcategory."""

from django.db import models


class Status(models.Model):
    """Модель статуса."""
    name = models.CharField(max_length=100, unique=True, verbose_name="Статус")

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"
        ordering = ['name']

    def __str__(self):
        """Возвращает название статуса."""
        return self.name


class Type(models.Model):
    """Модель типа."""
    name = models.CharField(max_length=100, unique=True, verbose_name="Тип")

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"
        ordering = ['name']

    def __str__(self):
        """Возвращает название типа."""
        return self.name


class Category(models.Model):
    """Модель категории."""
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        related_name='categories',
    )
    name = models.CharField(max_length=100, verbose_name="Категория")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['type__name', 'name']
        unique_together = ('type', 'name')

    def __str__(self):
        """Возвращает строковое представление категории."""
        return f"{self.type.name} → {self.name}"


class Subcategory(models.Model):
    """Модель подкатегории."""
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategories',
        verbose_name="Категория"
    )
    name = models.CharField(max_length=100, verbose_name="Подкатегория")

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        ordering = ['category__name', 'name']
        unique_together = ('category', 'name')

    def __str__(self):
        """Возвращает строковое представление подкатегории."""
        return f"{self.category.name} → {self.name}"
