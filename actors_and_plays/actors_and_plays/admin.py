from django.contrib import admin
from actors_and_plays.models import Actor, Role, Play, Director


admin.site.register(Actor)
admin.site.register(Role)
admin.site.register(Play)
admin.site.register(Director)
