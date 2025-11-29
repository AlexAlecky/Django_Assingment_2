from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ourFirstApp(request):
    return HttpResponse("Hello, this is our first app!")