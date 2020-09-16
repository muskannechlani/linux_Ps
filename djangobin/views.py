# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse
import subprocess

def index(request):
#    return HttpResponse("<p>Hello Django</p>")
     return render(request,'todo.html')
def runcommand(request):
    process = subprocess.Popen('ls', 
    shell=True, 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE )
    return HttpResponse(process.stdout)
def runcommand2(request):
    process = subprocess.Popen('ls -la', 
    shell=True, 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE )
    return HttpResponse(process.stdout)
# Create your views here.
