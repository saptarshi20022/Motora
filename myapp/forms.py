from datetime import date, timedelta
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class SignUpForm(UserCreationForm):
    username=forms.CharField(label="Enter user name*", widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter your user name'
        }))
    first_name = forms.CharField(label="Enter your first name*", widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter your first name'
        }))
    last_name = forms.CharField(label="Enter your last name*", widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter your last name'
        }))
    email = forms.CharField(label="Enter your email*", widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter your email'
        }))
    password1 = forms.CharField(label="Enter your password*", widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Enter your password'
        }))
    password2 = forms.CharField(label="Enter your confirm password*", widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Enter your confirm password'
        }))
    class Meta:
        model=User
        fields=['username','first_name','last_name', 'email']

class SignInForm(AuthenticationForm):
    username = forms.CharField(label="Enter user name*", widget=forms.TextInput(
        attrs={
            'class': 'form-control border-primary',
            'placeholder': 'Enter your username'
        }))
    password = forms.CharField(label="Enter your password*", widget=forms.PasswordInput(
        attrs={
            'class': 'form-control border-primary',
            'placeholder': 'Enter your password'
        }))

class BookingForm(forms.ModelForm):
    brand=forms.CharField(label="Enter vehicle brand name*", widget=forms.TextInput(
        attrs={
            'class': 'form-control border-primary',
            'placeholder': 'Enter vehicle brand name'
        }))
    modelname=forms.CharField(label="Enter vehicle model name*", widget=forms.TextInput(
        attrs={
            'class': 'form-control border-primary',
            'placeholder': 'Enter vehicle model name'
        }))
    mobile = forms.CharField(label="Enter your mobile number*", widget=forms.NumberInput(
        attrs={
            'class': 'form-control border-primary',
            'placeholder': 'Enter your mobile number'
        }))
    serviceDescriptions = forms.CharField(label="Describe problem in brief*", widget=forms.Textarea(
        attrs={
            'class': 'form-control border-primary',
            'placeholder': 'Describe problem in brief'
        }))

    servicingDate=forms.DateField(label="Select service date*",
            widget=DateInput(attrs={
            'class': 'form-control border-primary',
            'placeholder': 'Select service date'
        }))

    def clean_servicingDate(self):
        sd = self.cleaned_data['servicingDate']
        td=date.today()
        fd=date.today() + timedelta(days=20)
        if sd==td:
            raise forms.ValidationError('Selected date may not be today')
        elif sd < td:
            raise forms.ValidationError('Selected date may not be previous day')
        elif sd > fd:
            raise forms.ValidationError('Selected date must be within 20 days from current date')
        return sd
    class Meta:
        widgets={'servicingDate':DateInput()}
        model = Booking
        fields = ['bid','mobile', 'brand', 'modelname', 'serviceDescriptions', 'servicingDate']

