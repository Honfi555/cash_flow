"""Модель транзакции и связанные методы."""

from django.db import models
from django.utils import timezone

from catalog.models import Status, Type, Category, Subcategory


class Transaction(models.Model):
	"""Модель транзакции."""
	date = models.DateField(
		null=True,
		blank=True,
		verbose_name="Дата операции"
	)
	status = models.ForeignKey(
		Status,
		on_delete=models.PROTECT,
		verbose_name="Статус"
	)
	type = models.ForeignKey(
		Type,
		on_delete=models.PROTECT,
		verbose_name="Тип"
	)
	category = models.ForeignKey(
		Category,
		on_delete=models.PROTECT,
		verbose_name="Категория"
	)
	subcategory = models.ForeignKey(
		Subcategory,
		on_delete=models.PROTECT,
		verbose_name="Подкатегория"
	)
	amount = models.DecimalField(
		max_digits=10,
		decimal_places=2,
		verbose_name="Сумма"
	)
	comment = models.TextField(
		blank=True,
		verbose_name="Комментарий"
	)

	def save(self, *args, **kwargs):
		"""Сохраняет транзакцию; если дата не указана, устанавливает текущую дату."""
		if not self.date:
			self.date = timezone.now().date()
		super(Transaction, self).save(*args, **kwargs)

	class Meta:
		verbose_name = "Транзакция"
		verbose_name_plural = "Транзакции"
		ordering = ['-date']

	def __str__(self):
		"""Возвращает строковое представление транзакции."""
		return f"{self.date} | {self.type.name} | {self.amount}"
