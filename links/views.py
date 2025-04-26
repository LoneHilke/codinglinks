from django.shortcuts import render, redirect
from django.views import View
from .models import Python, Django, Link, Small

# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'links/forside.html')
    
class PythonView(View):
    def get(self, request, *args, **kwargs):
        python = Python.objects.all()
        context = {
        'python': python,
        } 
        return render(request, 'links/python.html', context)
    
class DjangoView(View):
    def get(self, request, *args, **kwargs):
        django = Django.objects.all()
        context ={
            'django':django
        }
        return render(request, 'links/django.html', context)
    
class Deploy(View):
    def get(self, request, *args, **kwargs):
        link = Link.objects.all()
        context = {
            'link':link
        }
        return render(request, 'links/deploy.html', context)
    
class Terminals(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'links/terminals.html')
    
class Info(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'links/info.html')
    
class SmallView(View):
    def get(self, request, *args, **kwargs):
        small = Small.objects.all()
        context = {
        'small': small,
        } 
        return render(request, 'links/kode.html', context)
    
class Microsoft(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'links/m365.html')