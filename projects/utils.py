from django.db.models import Q

from .models import Tag, Project

def searchProject(request):
    search_query = request
    tags = Tag.objects.filter(name__iexact=search_query)
    if search_query is not None:
        projects = Project.objects.distinct().filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(owner__name__icontains=search_query) |
            Q(tags__in=tags))
    else:
        projects = Project.objects.all()

    return projects, search_query