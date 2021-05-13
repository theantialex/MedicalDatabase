from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(Employee)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Medication)
admin.site.register(Procedure)


class PrescriptionAdmin(admin.ModelAdmin):
    raw_id_fields = ('appointment',)


class PerformedProceduresAdmin(admin.ModelAdmin):
    raw_id_fields = ('appointment',)


admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(PerformedProcedures, PerformedProceduresAdmin)