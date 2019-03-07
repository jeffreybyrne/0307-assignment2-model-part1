from django.contrib import admin
from food_reviews.models import Publication, Critic, Restaurant, Chef, Review

admin.site.register(Publication)
admin.site.register(Critic)
admin.site.register(Restaurant)
admin.site.register(Chef)
admin.site.register(Review)
