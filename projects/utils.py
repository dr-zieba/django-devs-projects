from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

from .models import Tag, Project


def searchProject(request):
    search_query = request.GET.get("search_query", "")
    tags = Tag.objects.filter(name__iexact=search_query)
    if search_query is not None:
        projects = Project.objects.distinct().filter(
            Q(title__icontains=search_query)
            | Q(description__icontains=search_query)
            | Q(owner__name__icontains=search_query)
            | Q(tags__in=tags)
        )
    else:
        projects = Project.objects.all()

    return projects, search_query


def pagePaginator(request, data, number_of_resuts_per_page):
    page_number = request.GET.get("page")
    paginator = Paginator(data, number_of_resuts_per_page)
    try:
        projects = paginator.page(page_number)
    except PageNotAnInteger:
        page_number = 1
        projects = paginator.page(page_number)
    except EmptyPage:
        page_number = paginator.num_pages
        projects = paginator.page(page_number)

    # SPlit paginator range for better visualisation
    l_index = int(page_number) - 4
    r_index = int(page_number) + 4
    if l_index < 1:
        l_index = 1
    if r_index > paginator.num_pages:
        r_index = paginator.num_pages + 1
    custom_range = range(l_index, r_index)
    projects = paginator.page(page_number)

    return custom_range, projects
