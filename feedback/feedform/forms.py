from django import forms
from django.contrib.auth.models import Group, User
from allauth.account.forms import LoginForm, ResetPasswordForm
from .models import Details

class NewLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(NewLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(
        	attrs={
        	'class':'form-control form-control-solid placeholder-no-fix',
        	'autocomplete': 'off',
        	'placeholder':"Username",
        	'name':'username'
        	})
        self.fields['password'].widget = forms.PasswordInput(
        	attrs={
        	'class':'form-control form-control-solid placeholder-no-fix',
        	'autocomplete': 'off',
        	'placeholder':"Password",
        	'name':'password'
        	})

class NewResetPasswordForm(ResetPasswordForm):
	def __init__(self, *args, **kwargs):
		super(NewResetPasswordForm, self).__init__(*args, **kwargs)
		self.fields['email'].widget = forms.EmailInput(
			attrs={
			'class':'form-control placeholder-no-fix',
			'placeholder':'email',
			'name':'email',
			})

class FeedBackForm(forms.ModelForm):
	class Meta:
		model= Details

		phone_number = forms.NumberInput(attrs={'minlength': 10, 'maxlength': 15, 'required': True}),
		comments = forms.CharField()
		fields= [
			'user',
			'phone_number',
			'neighbourhood',
			'rating',
			'comments'
		]