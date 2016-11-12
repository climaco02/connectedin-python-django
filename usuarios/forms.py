from django import forms
from django.contrib.auth.models import User

class RegistrarUsuarioForm(forms.Form):

	nome = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	senha = forms.CharField(required=True)
	telefone = forms.CharField(required=True)
	nome_empresa = forms.CharField(required=True)

	def is_valid():
		valid = True
		if not super(RegistrarUsuarioForm, self).is_valid():
			self.adiciona_erro('Por favor, verifique os dados informados')
			valid = False

		user_exists = User.objects.filter(username=self.data['email']).exists()

		if user_exists:
			self.adiciona_erro('Email ja cadastrado')
			valid = False

		return valid

	def adiciona_erro(self, message):
		erros = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, form.utils.ErrorsList())
		erros.append(message)