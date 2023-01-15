from django.shortcuts import render, redirect
from .models import Project, Review, Tag
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

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


@login_required(login_url="login")
def create_project(request):
    user = request.user.profile
    form = ProjectForm()
    context = {"form": form}

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = user
            project.save()
            return redirect("user-account")

    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def update_project(request, pk):
    user = request.user.profile
    project = user.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    context = {"form": form}

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("user-account")

    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def delete_project(request, pk):
    user = request.user.profile
    project = user.project_set.get(id=pk)
    context = {"object": project}

    if request.method == "POST":
        project.delete()
        return redirect("user-account")

    return render(request, "delete_object.html", context)
