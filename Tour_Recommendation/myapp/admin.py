from django.contrib import admin
from .models import Tour
# Register your models here.
@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('place','image')