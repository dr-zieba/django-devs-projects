from django.shortcuts import render, redirect
from .models import Project, Review, Tag
from .forms import ProjectForm

# Create your views here.
from django.http import HttpResponse


def projects(request):
    context = {"projects": Project.objects.all()}
    return render(request, "projects/projects.html", context)


def project(request, pk):
    project = Project.objects.get(id=pk)
    tags = project.tags.all()
    context = {"project": project, "tags": tags}
    return render(request, "projects/single-project.html", context)


def create_project(request):
    form = ProjectForm()
    context = {"form": form}

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("projects")

    return render(request, "projects/project_form.html", context)


def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    context = {"form": form}

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects")

    return render(request, "projects/project_form.html", context)


def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    context = {"object": project}

    if request.method == "POST":
        project.delete()
        return redirect("projects")

    return render(request, "projects/delete_object.html", context)