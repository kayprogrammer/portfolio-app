from django.shortcuts import render, redirect
from . import models
from django.utils import timezone
from portfolioss.models import Detail, Suscriber
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.urls import resolve
from .forms import *
import sweetify

# Create your views here.

@csrf_exempt
def home(request):

    form = SuscriberForm()
    if request.method == 'POST':
        form = SuscriberForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, title='Suscribed!',
                                     text='You have successfully suscribed to our newsletter. Thank you.',
                                     icon='success',
                                     button='Ok')
            return redirect('/')

    context = {'form':form}
    return render(request, 'portfolioss/main.html', context)

@csrf_exempt
def about(request):

    form = SuscriberForm()
    if request.method == 'POST':
        form = SuscriberForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, title='Suscribed!',
                                     text='You have successfully suscribed to our newsletter. Thank you.',
                                     icon='success',
                                     button='Ok')
            return redirect('about')

    context = {'form':form}
    return render(request, 'portfolioss/about.html', context)

@csrf_exempt
def services(request):

    form = SuscriberForm()
    form2 = DetailForm()
    if request.method == 'POST':
        try:
            if request.POST['name']:
                form2 = DetailForm(request.POST)
                if form2.is_valid():
                    form2.save()
                    sweetify.success(request, title='Message Received',
                                     text='Thank you for contacting us. We\'ll get back to you shortly.',
                                     icon='success',
                                     button='Ok', extra_tags='contact')
                    return redirect('services')

        except:
            form = SuscriberForm(request.POST)
            if form.is_valid():
                form.save()
                sweetify.success(request, title='Suscribed!',
                                     text='You have successfully suscribed to our newsletter. Thank you.',
                                     icon='success',
                                     button='Ok', extra_tags='suscribe')
                return redirect('services')
    
    context = {'form':form, 'form2':form2}
    return render(request, 'portfolioss/services.html', context)
