from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import AnimalForm
from .models import Animals


# Create your views here.
def ourFirstApp(request):
    return HttpResponse("Hello World welcome to our first app")


def home(request):
    return redirect('fetchAll')


def createAnimals(request):
    form = AnimalForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("fetchAll")
    context = {"form": form}
    return render(request, "forms.html", context)


def fetchAllAnimals(request):
    animals = Animals.objects.all()
    context = {"animals": animals}
    return render(request, "animals.html", context)


def Animals_detail(request, pk):
    animal = get_object_or_404(Animals, pk=pk)
    # provide both keys to be tolerant of templates
    context = {"animal": animal, "animals": animal}
    return render(request, 'animals_details.html', context)


def updateAnimals(request, pk):
    animal = get_object_or_404(Animals, pk=pk)
    form = AnimalForm(request.POST or None, instance=animal)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('fetchAll')
    return render(request, 'forms.html', {'form': form})


def deleteAnimals(request, pk):
    animal = get_object_or_404(Animals, pk=pk)
    if request.method == 'POST':
        animal.delete()
        return redirect('fetchAll')
    return render(request, 'animals_confirm_delete.html', {'animal': animal})