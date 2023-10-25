from django.contrib import admin
from .models import Cars

@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year')
