from django.contrib import admin
from people_with_addresses.models import Person, Residence, City, Province, Country


admin.site.register(Person)
admin.site.register(Residence)
admin.site.register(City)
admin.site.register(Province)
admin.site.register(Country)
