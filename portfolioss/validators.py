from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import ugettext as _
from .models import Suscriber

def fullnameValidator(value):
    if len(value) < 6:
        raise ValidationError(_('\'%(value)s\' is too short. (Use 6 chars or more)'), params={'value':value},)
    else:
        return value

full_regex_pattern = RegexValidator(regex=r'^[a-zA-Z]+\s[a-zA-Z]*$', message='Please input two names without digits or special characters.',)

email_regex_pattern = RegexValidator(regex=r"^[A-Za-z0-9]+[-_$.A-Za-z0-9]*@[A-Za-z0-9]*\.[A-Za-z]+$", message='Invalid email address')

def emailValidator(value):
    if Suscriber.objects.filter(email=value).exists():
        raise ValidationError("Suscriber with this Email already exists.")
    return value
