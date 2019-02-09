from django import forms
from django.core.files.images import get_image_dimensions

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user.models import UserProfile
from django.contrib.auth.forms import PasswordChangeForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('__all__')
    
class PasswordChangeCustomForm(PasswordChangeForm):
    error_css_class = 'has-error'
    error_messages = {'password_incorrect':
                "Mật khẩu cũ bạn nhập không đúng. Vui lòng nhập lại",
                'password_mismatch':"Mật khẩu mới không trùng nhau"
                }
    old_password = forms.CharField(required=True, label='Mật khẩu hiện tại',
                                   widget=forms.PasswordInput(attrs={
                    'class': 'form-control'}),
                    error_messages={
                    'required': 'Mật khẩu không được để trống.'})

    new_password1 = forms.CharField(required=True, label='Mật khẩu mới',
                                    widget=forms.PasswordInput(attrs={
                    'class': 'form-control'}),
                    error_messages={
                    'required': 'Mật khẩu không được để trống.'})
    new_password2 = forms.CharField(required=True, label='Mật khấu mới (Nhập lại)',
                                    widget=forms.PasswordInput(attrs={
                    'class': 'form-control'}),
                    error_messages={
                    'required': 'Mật khẩu không được để trống.'})
