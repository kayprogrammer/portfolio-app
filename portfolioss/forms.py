from django.forms import ModelForm
from . models import *
from django import forms
from . validators import *

class SuscriberForm(ModelForm):
    email = forms.CharField(max_length=100, label=False, validators= [email_regex_pattern, emailValidator], widget=forms.EmailInput(attrs={'placeholder':'Enter your email address', 'type':'email'}))

    class Meta:
        model = Suscriber
        fields = '__all__'

class DetailForm(ModelForm):
    name = forms.CharField(max_length=100, validators=[full_regex_pattern, fullnameValidator], label=False, widget=forms.TextInput(attrs={'placeholder':'Full Name...', 'type':'name'}))
    email = forms.CharField(max_length=100, label=False, validators= [email_regex_pattern], widget=forms.EmailInput(attrs={'placeholder':'Email Address...', 'class':'form2', 'type':'email'}))
    text = forms.CharField(max_length=100, label=False, widget=forms.Textarea(attrs={'placeholder':'Message...', 'type':'text', 'class':'form2', 'rows':5}))

    class Meta:
        model = Detail
        fields = '__all__'