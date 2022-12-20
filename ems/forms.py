from django import forms

class CreateForm(forms.Form):
    name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'Enter Your Name'}),label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter the Password'}), label='')
    mobile = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Mobile'}),max_length=10, label='')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email'}),max_length=200, label='')

class LoginForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Name'}),max_length=20, label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter the Password'}), label='')

class EditNameForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter The New Name'}),max_length=20, label='')

class EditPassForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter the Password'}), label='')
