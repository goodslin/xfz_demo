from django import forms
from django.core import validators
from . import models


class MessageBoardFrom(forms.Form):
    title = forms.CharField(max_length=32, min_length=6, label='标题')
    content = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    reply = forms.BooleanField(required=False)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=32, label='姓名')
    telephone = forms.CharField(max_length=16, validators=[validators.RegexValidator(
        r'^((13[0-9])|(14[5,7])|(15[0-3,5-9])|(17[0,3,5-8])|(18[0-9])|166|198|199|(147))\d{8}$')],
                                error_messages={'invalid': '请输入正确的手机号码'})
    pwd1 = forms.CharField(max_length=32, min_length=8)
    pwd2 = forms.CharField(max_length=32, min_length=8)

    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        exist = models.User.objects.filter(telephone=telephone).exists()
        if exist:
            raise forms.ValidationError("%s已经被注册" % telephone)
        return telephone

    def clean(self):
        # 如果到达clean方法，说明之前每一个字段都验证成功了。
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError('两次密码不一致')
        return cleaned_data

    def get_errors(self):
        errors = self.errors.get_json_data()
        new_errors = {}
        for key, message_dicts in errors.items():
            messages = []
            for message_dict in message_dicts:
                message = message_dict['message']
                messages.append(message)
            new_errors[key] = messages
        return new_errors


class AddBookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = "__all__"
        # fields = ['title', 'page']
        # exclude = ['price']
        error_messages = {
            'page': {
                'required': '请传入page参数',
                'invalid': '请输入一个可用的page',
            },
            'title': {
                'max_length': 'title不能超过64个字段',
            },
            'price': {
                'max_value': '图书价格不能超过100元。'
            }
        }


