from django.urls import path
from . import views

app_name = 'voice'
urlpatterns = [
    path('', views.index, name='index'),
    path('doctor_access/<int:doctorid>/<int:userid>', views.doctor_access, name='doctor_access'),
    path('prescriptions/<int:patientid>', views.user_prescriptions, name='user_prescriptions'),
    path('prescription_details/<int:prescriptionid>', views.prescription_details, name='prescription_details'),
    path('add_prescription/<int:patientid>', views.add_prescription, name='add_prescription'),
    path('patient_history/<int:patientid>', views.patient_history, name='patient_history')
]
