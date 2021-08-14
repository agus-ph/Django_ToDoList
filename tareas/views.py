from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Tareas
from .forms import TareasForm

# Create your views here.


def index(
    request,
):
    tareas = Tareas.objects.all()

    form = TareasForm()

    if request.method == "POST":
        form = TareasForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {"tareas": tareas, "form": form}
    return render(request, "tareas/lista.html", context)


def actualiza_tarea(
    request,
    pk,
):
    tarea = Tareas.objects.get(id=pk)

    form = TareasForm(instance=tarea)

    if request.method == "POST":
        form = TareasForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"form": form}

    return render(request, "tareas/actualiza_tarea.html", context)


def eliminar_tarea(
    request,
    pk,
):
    item = Tareas.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect("/")

    context = {"item": item}
    return render(request, "tareas/eliminar.html", context)