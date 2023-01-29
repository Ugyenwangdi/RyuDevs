from .models import Profile, Skill
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateProfiles(request, profiles, results):

    page = request.GET.get('page')
    
    paginator = Paginator(profiles, results)

    try: 
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)

    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    leftIndex = (int(page) - 4)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, profiles
def searchProfiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(name__icontains=search_query)
    

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) | 
        Q(short_intro__icontains=search_query) |
        Q(skill__in=skills)        
    )

    bhutan_locations = ['Bhutan', 'Bumthang', 'Chukha','Chhukha', 'Dagana', 'Gasa', 'Haa', 'Lhuntse', 
                'Mongar', 'Paro', 'Pemagatshel', 'Punakha', 'Samdrup Jongkhar', 'Samtse', 
                'Sarpang', 'Thimphu', 'Trashigang', 'Trashiyangtse', 'Trongsa', 'Tsirang', 
                'Wangdue Phodrang', 'Zhemgang']

    profiles_bhutanese = []

    for profile in profiles:
        if profile.dzongkhag:
            for place in profile.dzongkhag.split(','):
                if place in bhutan_locations:
                    profiles_bhutanese.append(profile)


    return profiles_bhutanese, search_query 

    