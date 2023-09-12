from typing import Any, Dict
from django import forms
from .models import User
from argon2 import exceptions, PasswordHasher
from django.db import IntegrityError
from django.http import JsonResponse

class JoinForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'start_period',
            'end_period'
        ]
    #유효성 검사하는 clean 매소드
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username', '')
        password1 = cleaned_data.get('password1', '')
        password2 = cleaned_data.get('password2', '')
        start_period = cleaned_data.get('start_period','')
        end_period = cleaned_data.get('end_period', '')
            
        if password1 != password2:
            return self.add_error('password2', '비밀번호가 다릅니다')
        # elif IntegrityError:
        #     return self.add_error('username', '중복된 사용자 입니다')
        else : 
            self.username = username
            self.password1 = PasswordHasher().hash(password1)
            self.password2 = password2
            self.start_period = start_period
            self.end_period = end_period        

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=32,
        label='아이디',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'username',
                'placeholder' : '아이디'
            }
        ),
    )
    password = forms.CharField(
        max_length=100,
        label='비밀번호',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'password',
                'placeholder' : '비밀번호'
            }
        ),
    )

    def clean(self):
        cleand_data = super().clean()

        username = cleand_data.get('username', '')
        password = cleand_data.get('password', '')

        if username == '':
            return self.add_error('username', '아이디를 다시 입력해주세요')
        elif password == '':
            return self.add_error('password', '비밀번호를 다시 입력해 주세요')
        else:
            try:
                user = User.objects.get(username = username)
            except User.DoesNotExist:
                return self.add_error('username', '아이디가 존재하지 않습니다. ')
            
            try:
                PasswordHasher().verify(user.password, password)
            except exceptions.VerifyMismatchError:
                return self.add_error('password', '비밀번호가 다릅니다.')
            
            self.login_session = user.username
            self.username = user.username