from django import forms
from .models import User


class RegisterForm(forms.ModelForm):
    password_repeat = forms.CharField(max_length=32)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')
        if password != password_repeat:
            raise forms.ValidationError('两次输入密码不一致')
        return cleaned_data

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']


class TransferForm(forms.Form):
    email = forms.CharField(max_length=32)
    money = forms.FloatField()
