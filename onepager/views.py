from django.shortcuts import render

def home(request):
    return render(request, 'onepager/index.html') 