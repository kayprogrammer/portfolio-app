from django.contrib import admin
from .models import Detail, Suscriber

# Register your models here.
myModels = [Detail, Suscriber]  # iterable list
admin.site.register(myModels)