from django.shortcuts import render, redirect
from .models import Community, Language, Country, Suburblocation, School, Hospital
from lockdown.decorators import lockdown
from .utils import Sendmail
from common import settings
import csv, requests, json


def index(request):
    return render(request, "community/index.html", {})


def error_400(request, exception):
    return render(request, "community/error400.html", status=400)


def error_403(request, exception):
    return render(request, "community/error403.html", status=403)


def error_404(request, exception):
    return render(request, "community/error404.html", status=404)


def error_500(request, exception):
    return render(request, "community/error500.html", status=500)


def search_suburb(request):
    return render(request, "community/search.html", {})


def about_us(request):
    return render(request, "community/aboutus.html", {})


def immunization(request):
    return render(request, "community/immunization.html", {})

def sendemail(request):
    return render(request, "community/sendemail.html", {})


def detail(request):
    name = request.GET.get('name')
    postcode = name[-4:]
    name = name[:-5]
    community_list = Community.objects.filter(name__iexact=name)
    result_list = []
    for community in community_list:
        language_list = Language.objects.filter(community=community)
        language_spoken = []
        for language in language_list:
            if language.language == 'English':
                continue
            language_spoken.append((language.language, language_per_community(language)))
        language_spoken.sort(key=lambda x: x[1], reverse=True)
        if len(language_spoken) > 10:
            language_spoken = language_spoken[:10]
        result_list.append((community, language_spoken, postcode))
    return render(request, "community/detail.html", {"result_list": result_list})


def compare(request):
    if request.method == "GET":
        community_strs = request.GET.getlist('compare_list', [])
        country = request.GET.get('country_select')
        my_language = request.GET.get('language_select')
        subloca_list = []
        for community_str in community_strs:
            communities = Community.objects.filter(name=community_str.split('+')[0])
            for community in communities:
                suburb_location = Suburblocation.objects.get(community=community, postcode=community_str.split('+')[1])
                subloca_list.append(suburb_location)
        country_list = Country.objects.filter(country=country)
        language_spoken_in_my_country = []
        for cty in country_list:
            if cty.language.language != my_language:
                language_spoken_in_my_country.append(cty.language.language)
        result_list = []
        for suburb_location in subloca_list:
            language_spoken = []
            homeland_lng = ()
            language_list = Language.objects.filter(community=suburb_location.community)
            for language in language_list:
                if language.language in language_spoken_in_my_country:
                    language_spoken.append((language.language, language_per_community(language)))
                if language.language == my_language:
                    homeland_lng = (my_language, str(language_per_community(language)))
            language_spoken.sort(key=lambda x: x[1], reverse=True)
            language_spoken = [(language[0], str(language[1])) for language in language_spoken]
            result_list.append((suburb_location.community, language_spoken, homeland_lng, str(suburb_location.postcode), country))
    if request.method == "POST":
        email = request.POST.get('email').strip()
        name = request.POST.getlist('name')
        postcode = request.POST.getlist('postcode')
        mylng = request.POST.get('mylng')
        homeland = request.POST.getlist('homeland')
        overseas = request.POST.getlist('overseas')
        noneng = request.POST.getlist('noneng')
        first_name = request.POST.getlist('first_name')
        second_name = request.POST.getlist('second_name')
        third_name = request.POST.getlist('third_name')
        forth_name = request.POST.getlist('forth_name')
        first_per = request.POST.getlist('first_per')
        second_per = request.POST.getlist('second_per')
        third_per = request.POST.getlist('third_per')
        forth_per = request.POST.getlist('forth_per')
        kindergarten = request.POST.getlist('kindergarten')
        primary = request.POST.getlist('primary')
        secondary = request.POST.getlist('secondary')
        p12 = request.POST.getlist('p12')
        mental = request.POST.getlist('mental')
        dental = request.POST.getlist('dental')
        gp = request.POST.getlist('gp')
        pharmacy = request.POST.getlist('pharmacy')
        allied = request.POST.getlist('allied')
        complementary = request.POST.getlist('complementary')
        disability = request.POST.getlist('disability')
        residential = request.POST.getlist('residential')

        Sendmail.send(email, name, postcode, mylng, homeland, overseas, noneng, first_name, second_name, third_name,
                 forth_name,
                 first_per, second_per, third_per, forth_per, kindergarten, primary, secondary, p12, mental,
                 dental, gp, pharmacy, allied, complementary, disability, residential)
        return render(request, 'community/sendemail.html', {"email": email})
    return render(request, 'community/compare.html',
                  {"result_list": result_list, "filters": request.GET.getlist("filters_select", [])})



def search_result(request):
    name = request.GET.get('name')
    postcode = request.GET.get('postcode')
    country = request.GET.get('country')
    my_language = request.GET.get('language')
    country_list = Country.objects.filter(country=country)
    language_spoken_in_my_country = []
    for cty in country_list:
        if cty.language.language != my_language:
            language_spoken_in_my_country.append(cty.language.language)
    community_list = Community.objects.filter(name__iexact=name)
    result_list = []
    for community in community_list:
        language_spoken = []
        homeland_lng = ()
        language_list = Language.objects.filter(community=community)
        for language in language_list:
            if language.language in language_spoken_in_my_country:
                language_spoken.append((language.language, language_per_community(language)))
            if language.language == my_language:
                homeland_lng = (my_language, language_per_community(language))
        language_spoken.sort(key=lambda x: x[1], reverse=True)
        result_list.append((community, language_spoken, homeland_lng, postcode, country))
    return render(request, "community/result.html", {"result_list": result_list})


def language_per_community(language):
    sum = 0
    for lng in Language.objects.filter(community=language.community):
        sum = sum + lng.count
    return round(language.count / sum * 100, 2)


def findsuburb(request):
    country_dict = {}
    for country_language in Country.objects.all():
        if country_language.country not in country_dict.keys():
            country_dict[country_language.country] = []
        country_dict[country_language.country].append(country_language.language.language)
    if request.method == "POST":
        ordered_lng = []
        filters = request.POST.getlist("filters", [])
        language_read = request.POST.get("language", "")
        language_list = Language.objects.filter(language__iexact=language_read)
        for language in language_list:
            community = language.community
            add = True
            for filter in filters:
                if getattr(community, filter) == 0:
                    add = False
                    break
            if add:
                ordered_lng.append(language)
        ordered_lng.sort(key=language_per_community, reverse=True)
        result_list = []
        for language in ordered_lng:
            suburblocation_list = Suburblocation.objects.filter(community=language.community)
            for suburblocation in suburblocation_list:
                result_list.append(suburblocation)
        return render(request, 'community/findsuburb.html', {"country_dict": country_dict,
                                                             "result_list": result_list,
                                                             "post": True,
                                                             "country": request.POST.get("country", ""),
                                                             "language": language_read,
                                                             "filters": filters})
    return render(request, 'community/findsuburb.html', {"country_dict": country_dict, "post": False})



def map(request):
    base = "/home/ryanchen0008/vic-migrant-health/"
    relative = "community/static/community/js/vic.json"
    path = relative
    path = base + relative
    boundary_json = json.load(open(path))
    QUERY_NEARBY = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
    name = request.GET.get('name')
    postcode = request.GET.get('postcode')
    boundary = None
    for suburb in boundary_json:
        if suburb['properties']['Suburb_Name'].strip() == name:
            boundary = suburb
            break
    community = Community.objects.filter(name__iexact=name).first()
    location = Suburblocation.objects.get(community=community, postcode=postcode)
    medical_query = QUERY_NEARBY + 'location=' + str(location.latitude) + ',' + str(location.longitude) + '&radius=1500&type=doctor&type=hospital' + '&key=' + settings.GOOGLE_MAPS_API_KEY
    dentist_query = QUERY_NEARBY + 'location=' + str(location.latitude) + ',' + str(location.longitude) + '&radius=1500&type=dentist' + '&key=' + settings.GOOGLE_MAPS_API_KEY
    r_med = requests.get(medical_query)
    r_den = requests.get(dentist_query)
    medicals = []
    dentists = []
    if r_med.status_code == 200:
        med_array = r_med.json()['results']
        for med in med_array:
            medicals.append(med['place_id'])
    if r_den.status_code == 200:
        den_array = r_den.json()['results']
        for den in den_array:
            dentists.append(den['place_id'])
    hospitals = []
    primaries = []
    secondaries = []
    pri_secs = []
    specials = []
    hospital_list = Hospital.objects.filter(suburb=community.name, postcode=postcode)
    for hos in hospital_list:
        hospitals.append({'name': hos.name, 'type': hos.type, 'address_line': hos.street_number + ' ' + hos.road_name + ' ' + hos.road_type, 'address_town': hos.suburb, 'postcode': hos.postcode, 'latitude': hos.latitude, 'longitude': hos.longitude})
    primary_list = School.objects.filter(type='Primary', postcode=postcode)
    for pri in primary_list:
        primaries.append({'name':pri.name, 'type':pri.type, 'address_line':pri.address_line, 'address_town':pri.address_town, 'postcode':pri.postcode, 'contact':pri.contact, 'education_sector':pri.education_sector, 'latitude':pri.latitude, 'longitude':pri.longitude})
    secondary_list = School.objects.filter(type='Secondary', postcode=postcode)
    for sec in secondary_list:
        secondaries.append({'name':sec.name, 'type':sec.type, 'address_line':sec.address_line,  'address_town':sec.address_town, 'postcode':sec.postcode, 'contact':sec.contact, 'education_sector':sec.education_sector, 'latitude':sec.latitude, 'longitude':sec.longitude})
    pri_sec_list = School.objects.filter(type='Pri/Sec', postcode=postcode)
    for p_s in pri_sec_list:
        pri_secs.append({'name':p_s.name, 'type':p_s.type, 'address_line':p_s.address_line, 'address_town':p_s.address_town, 'postcode':p_s.postcode, 'contact':p_s.contact, 'education_sector':p_s.education_sector, 'latitude':p_s.latitude, 'longitude':p_s.longitude})
    special_list = School.objects.filter(type='Special', postcode=postcode)
    for spe in special_list:
        specials.append({'name':spe.name, 'type':spe.type, 'address_line':spe.address_line, 'address_town':spe.address_town, 'postcode':spe.postcode, 'contact':spe.contact, 'education_sector':spe.education_sector, 'latitude':spe.latitude, 'longitude':spe.longitude})
    return render(request, "community/map.html", {"api_key": settings.GOOGLE_MAPS_API_KEY,
                                                  "location": location,
                                                  "boundary": boundary,
                                                  "hospitals": hospitals,
                                                  "medicals": medicals,
                                                  "dentists": dentists,
                                                  "primary": primaries,
                                                  "secondary": secondaries,
                                                  "pri_sec": pri_secs,
                                                  "special": specials})



def readHospital(request):
    with open("community/static/community/csv/hospital_locations.csv") as f:
        reader = csv.reader(f)
        header = True
        for row in reader:
            if header:
                header = False
            else:
                _, created = Hospital.objects.get_or_create(
                    name=row[2],
                    type=row[3],
                    street_number=row[4],
                    road_name=row[5],
                    road_type=row[6],
                    suburb=row[7],
                    postcode=row[9],
                    latitude=row[1],
                    longitude=row[0],
                )
    return render(request, "community/index.html", {})



def readSchool(request):
    with open("community/static/community/csv/school_location_data.csv") as f:
        reader = csv.reader(f)
        header = True
        for row in reader:
            if header:
                header = False
            else:
                _, created = School.objects.get_or_create(
                    education_sector=row[0],
                    name=row[1],
                    type=row[2],
                    address_line=row[3],
                    address_town=row[4],
                    postcode=row[5],
                    contact=row[6],
                    latitude=row[8],
                    longitude=row[7],
                )
    return render(request, "community/index.html", {})



def readLanguage(request):
    with open("community/static/community/csv/suburb_language_count.csv") as f:
        reader = csv.reader(f)
        header = True
        for row in reader:
            if header:
                header = False
            else:
                community_read = Community.objects.filter(name=row[0]).first()
                if community_read:
                    _, created = Language.objects.get_or_create(
                        community=community_read,
                        language=row[1],
                        count=row[2],
                        sub_location=row[3],
                    )
    return render(request, "community/index.html", {})


def readCountry(request):
    with open("community/static/community/csv/language_per_country.csv") as f:
        reader = csv.reader(f)
        header = True
        for row in reader:
            if header:
                header = False
            else:
                language_read = Language.objects.filter(language=row[1]).first()
                if language_read:
                    _, created = Country.objects.get_or_create(
                        language=language_read,
                        country=row[0],
                        code=row[2],
                    )
    return render(request, "community/index.html", {})


def readSuburbLocation(request):
    with open("community/static/community/csv/suburb_location.csv") as f:
        reader = csv.reader(f)
        header = True
        for row in reader:
            if header:
                header = False
            else:
                community_read = Community.objects.filter(name=row[1]).first()
                if community_read:
                    _, created = Suburblocation.objects.get_or_create(
                        postcode=row[0],
                        community= community_read,
                        latitude=row[4],
                        longitude=row[5],
                    )
    return render(request, "community/index.html", {})


def readCommunity(request):
    with open("community/static/community/csv/town_community_profile.csv") as f:
        reader = csv.reader(f)
        header = True
        for row in reader:
            if header:
                header = False
            else:
                _, created = Community.objects.get_or_create(
                    name=row[0],
                    type=row[1],
                    density=row[2],
                    area=row[3],
                    kindergarten=row[15],
                    primary_school=row[18],
                    secondary_school=row[19],
                    p12_school=row[20],
                    other_school=row[21],
                    born_overseas=row[24],
                    except_eng=row[25],
                    culture_group1_name=row[26],
                    culture_group2_name=row[28],
                    culture_group3_name=row[30],
                    culture_group4_name=row[32],
                    culture_group1_per=row[27],
                    culture_group2_per=row[29],
                    culture_group3_per=row[31],
                    culture_group4_per=row[33],
                    child_protection=row[4],
                    community_health=row[5],
                    homeless=row[6],
                    disability=row[7],
                    mental_health=row[8],
                    human=row[9],
                    dental=row[10],
                    general_practice=row[11],
                    pharmacy=row[12],
                    allied_health=row[13],
                    complementary_health=row[14],
                    residential_aged_care=row[16],
                    licensed_aged_care=row[17],
                    nearest_health=row[22],
                    dis_nearest_health=row[23],
                )
    return render(request, "community/index.html", {})

