from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def scram(request):
    data = request.POST.get("Phrase")
    print(data)
    return render(request, 'revealing/index.html', {'data' : data})