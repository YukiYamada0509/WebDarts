from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.conf.urls import url, static

# Create your views here.

@login_required
def index(request):
    return render(request, 'home/index.html')
