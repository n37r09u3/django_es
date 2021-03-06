from django.contrib import admin
from .models import Car


@admin.register(Car)
class CompanyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Car._meta.fields]

