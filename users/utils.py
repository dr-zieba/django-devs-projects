from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from .models import Profile, Skill


def searchUser(request):
    seaerch_query = request.GET.get("search_query", "")
    skills = Skill.objects.filter(name__iexact=seaerch_query)
    if seaerch_query is not None:
        profiles = Profile.objects.distinct().filter(
            Q(name__icontains=seaerch_query)
            | Q(short_info__icontains=seaerch_query)
            | Q(skill__in=skills)
        )
    else:
        profiles = Profile.objects.all().order_by("-name").values()

    return profiles, seaerch_query


def usersPaginator(request, data, number_of_resuts_per_page):
    page_number = request.GET.get("page")
    paginator = Paginator(data, number_of_resuts_per_page)
    try:
        users = paginator.page(page_number)
    except PageNotAnInteger:
        page_number = 1
        users = paginator.page(page_number)
    except EmptyPage:
        page_number = paginator.num_pages
        users = paginator.page(page_number)

    # SPlit paginator range for better visualisation
    l_index = int(page_number) - 4
    r_index = int(page_number) + 4
    if l_index < 1:
        l_index = 1
    if r_index > paginator.num_pages:
        r_index = paginator.num_pages + 1
    custom_range = range(l_index, r_index)
    users = paginator.page(page_number)

    return custom_range, users
