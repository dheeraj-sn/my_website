from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, Http404, HttpResponseRedirect
# Create your views here.

def Index(request):
    return render(request, 'resume/index.html')
