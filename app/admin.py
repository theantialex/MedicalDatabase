from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(Employee)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Medication)
admin.site.register(Procedure)
admin.site.register(Prescription)
admin.site.register(PerformedProcedures)