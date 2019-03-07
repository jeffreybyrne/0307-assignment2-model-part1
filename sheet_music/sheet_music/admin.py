from django.contrib import admin
from sheet_music.models import Music, Sheet, Instrument

admin.site.register(Music)
admin.site.register(Sheet)
admin.site.register(Instrument)
