from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import Project, Review, Tag
from .forms import ProjectForm, ReviewForm
from django.contrib.auth.decorators import login_required
from .utils import searchProject, pagePaginator
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
from django.http import HttpResponse


def projects(request):
    projects, search_query = searchProject(request)
    custom_range, projects = pagePaginator(request, projects, 6)
    context = {
        "projects": projects,
        "search_query": search_query,
        "custom_range": custom_range,
    }

    return render(request, "projects/projects.html", context)


def project(request, pk):
    project = Project.objects.get(id=pk)
    tags = project.tags.all()
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            try:
                review = form.save(commit=False)
                review.project = project
                review.owner = request.user.profile
                review.save()

                project.getVoteCount

                messages.success(request, "Comment added")
                return redirect("project", pk=pk)
            except IntegrityError:
                messages.error(request, "Vote already added!!!")
                return redirect("project", pk=pk)

    context = {"project": project, "tags": tags, "form": form}
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
