"""Вьюхи для управления аккаунтами пользователей (регистрация и т.д.)."""

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class RegisterView(generic.CreateView):
	"""Вью для регистрации нового пользователя."""

	form_class = UserCreationForm
	template_name = 'accounts/register.html'
	success_url = reverse_lazy('transactions:list')

	def form_valid(self, form):
		"""
		Обрабатывает валидную форму регистрации:
		сохраняет пользователя и выполняет вход.
		"""
		response = super().form_valid(form)
		# сразу логиним нового пользователя
		user = form.save()
		login(self.request, user)
		return response
