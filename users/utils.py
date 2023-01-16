from django.db.models import Q
from .models import Profile, Skill

def searchUser(request):
    seaerch_query = request
    skills = Skill.objects.filter(name__iexact=seaerch_query)
    if seaerch_query is not None:
        profiles = Profile.objects.distinct().filter(
            Q(name__icontains=seaerch_query) |
            Q(short_info__icontains=seaerch_query) |
            Q(skill__in=skills))
    else:
        profiles = Profile.objects.all().order_by('-name').values()

    return profiles, seaerch_query