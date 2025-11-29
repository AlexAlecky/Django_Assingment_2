from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import AnimalForm
from .models import Animal



# Create your views here.
def ourFirstApp(request):
    return render(request, 'firstApp/main.html')

def home(request):
    return redirect('fetchAll')


def createAnimal(request):
    form = AnimalForm()
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request,'firstApp/forms.html', context) 

def fetchAllAnimals(request):
    animals = Animal.objects.all()
    context = {'animals': animals}
    return render(request, 'firstApp/home.html', context)