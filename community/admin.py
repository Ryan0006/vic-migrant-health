from django.contrib import admin
from .models import Community, Language, Country, Suburblocation, School, Hospital

admin.site.register(Community)
admin.site.register(Language)
admin.site.register(Country)
admin.site.register(Suburblocation)
admin.site.register(School)
admin.site.register(Hospital)