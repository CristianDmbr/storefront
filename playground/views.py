from django.shortcuts import render
from django.http import HttpResponse



def sayHello(request):
    return render(request, 'hello.html',{'name':'Mosh'})