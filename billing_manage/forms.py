'''
Code description:
Create time: 2020/12/16
Developer: 叶修
'''

from django import forms
from django.forms import widgets
from createdatabase.models import Manage

class LoginForm(forms.Form):
    user_name = forms.CharField(required=True,label='用户名',error_messages={'required':'用户名不能为空'},
                               widget=widgets.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(required=True,label='密码',error_messages={'required':'密码不能为空',
                                                                         'maxlength':'密码最大长度8位',
                                                                         'minLength':'密码最小长度4位'},
                               max_length=8,
                               min_length=4,
                               widget = widgets.PasswordInput(attrs={'class':'form-control','placeholder':'请输入4-8位密码'}))
class SignUpForm(forms.Form):
    user_name = forms.CharField(required=True,label='用户名',error_messages={'required':'用户名不能为空'},
                               widget = widgets.TextInput(attrs={'style':'font-size:16px;height:25px'}))
    login_name = forms.CharField(required=True,label='昵称',error_messages={'required':'昵称不能为空'},
                                 widget=widgets.TextInput(
                                     attrs={'class':'form-control','style':'font-size:16px;height:25px;'}))

    password = forms.CharField(required=True,
                               label='密码',
                               error_messages={'required':'密码不能为空',
                                               'max_length':'密码最大长度8位',
                                               'min_length':'密码最小长度4位'},
                               max_length=8,
                               min_length=4,
                               widget=widgets.PasswordInput(
                               attrs={'class':'pwd','placeholder':'请输入4-8位密码','style':'font-size:16px;height:25px;'}))

    repassword = forms.CharField(required=True,
                                 label='确认密码',
                                 error_messages={'required':'确认密码不能为空',
                                                 'max_length':'密码最大长度8位',
                                                 'min_length':'密码最小长度4位'},
                                 max_length=8,
                                 min_length=4,
                                 widget=widgets.PasswordInput(
                                     attrs={'class': 'pwd', 'placeholder': '请输入4-8位密码',
                                            'style': 'font-size:16px;height:25px;'}))
