from django.contrib import admin

# Register your models here.
from PATIENT.models import *
admin.site.register(Patient)
admin.site.register(Invoice)