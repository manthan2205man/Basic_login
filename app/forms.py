from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class SchoolAdminForm(UserCreationForm):
    username = forms.EmailField(label='Email-id',widget=forms.TextInput(attrs={'placeholder': 'Please Enter Email'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Password Should be character+number+symbol lenght(8-13)'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Please Re-Enter Password'}))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'placeholder': 'Please Enter First Name'}),required=True)
    last_name = forms.CharField(label='Last Name',widget=forms.TextInput(attrs={'placeholder': 'Please Enter Last Name'}))
    phone = forms.IntegerField(label='Mobile Number',widget=forms.TextInput(attrs={'placeholder': 'Please Enter 10 digit Mobile number'}))

    class Meta:
        model=get_user_model()
        fields=('first_name','last_name','username','password1','password2','phone')


class StudentForm(UserCreationForm):
    username=forms.EmailField(label='Email-id',widget=forms.TextInput(attrs={'placeholder': 'Please Enter Email'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Password Should be character+number+symbol lenght(8-13)'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Please Re-Enter Password'}))
    first_name = forms.CharField(label='First Name',widget=forms.TextInput(attrs={'placeholder': 'Please Enter First Name'}))
    last_name = forms.CharField(label='Last Name',widget=forms.TextInput(attrs={'placeholder': 'Please Enter Last Name'}))
    phone = forms.IntegerField(label='Mobile Number',widget=forms.TextInput(attrs={'placeholder': 'Please Enter 10 digit Mobile number'}),validators=[RegexValidator(regex='\d{10}',message='invalid number',code='invalid_number')])
    roll_no = forms.IntegerField(label='Roll Number',widget=forms.TextInput(attrs={'placeholder': 'Please Enter your roll number'}))

    class Meta:
        model=get_user_model()
        fields=('first_name','last_name','username','password1','password2','phone','roll_no',)


class TextnotesForm(forms.ModelForm):
    # student = forms.MultipleChoiceField(choices=[(option, option) for option in
    #          User.objects.filter(is_student=True)], widget=forms.CheckboxSelectMultiple(),)
    class Meta:
        model=Textnotes
        fields=['textnotes','student']
