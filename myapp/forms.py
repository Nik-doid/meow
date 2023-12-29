from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class RegistrationForm(forms.ModelForm):
    roll_number = forms.CharField(max_length=255, required=True, help_text='Required. Enter your roll number.')
    name = forms.CharField(max_length=255, required=True, help_text='Required. Enter your full name.')
    age = forms.IntegerField(required=True, help_text='Required. Enter your age.')
    parents_number = forms.CharField(max_length=15, required=True, help_text='Required. Enter your parents\' phone number.')

    class Meta:
        model = CustomUser
        fields = ['roll_number', 'name', 'age', 'parents_number']

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age and age <= 1:
            raise forms.ValidationError("Age must be above 1.")
        return age


