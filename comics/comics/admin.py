from django.contrib import admin
from comics.models import Artist, Comic, Issue, Writer

admin.site.register(Comic)
admin.site.register(Artist)
admin.site.register(Writer)
admin.site.register(Issue)
