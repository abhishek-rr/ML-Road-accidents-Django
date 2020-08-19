from django.shortcuts import render

def home(request):
    return render(request,'Home.html',{'a':1234})  