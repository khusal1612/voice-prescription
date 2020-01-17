from django.contrib import admin
from .models import Hospital, Patient, AccessRequest, HospitalAccess

admin.site.register(Hospital)
admin.site.register(Patient)
admin.site.register(AccessRequest)
admin.site.register(HospitalAccess)
