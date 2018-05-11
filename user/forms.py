from django import forms
from django.core.files.images import get_image_dimensions

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user.models import Teacher, UserProfile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('__all__')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('__all__')
    