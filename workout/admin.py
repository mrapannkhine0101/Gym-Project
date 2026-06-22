from collections.abc import Set

from django.contrib import admin
from .models import Workout, Profile

# Register your models here.
admin.site.register(Workout)
admin.site.register(Profile)

    