from django.shortcuts import render
from django.http import HttpResponse
import json

def index(request):
    return HttpResponse(json.dumps({'status':'success'}))

def doctor_access(request, doctorid, userid):
    data = {
        'status' : 'requested'
    }
    return HttpResponse(json.dumps(data))

def prescription_details(request, prescriptionid):
    data = {
        'id': patientid,
        'medicines': [
            {'name':'paracetamol', 'frequency':2, 'instructions': 'before meal'},
            {'name':'saridon', 'frequency':2, 'instructions': 'after meal'}
        ],
        'diagnostics': [
            {'name':'x ray', 'details': 'before meal'},
            {'name':'saridon', 'details': 'after meal'}
        ]
    }
    return HttpResponse(json.dumps(data))

def user_prescriptions(request, patientid):
    data = [
        {'name': 'bmb hospital', 'hospital_id': '1', 'purpose': 'nothing'},
        {'name': 'bmb2 hospital', 'hospital_id': '2', 'purpose': 'nothing1'},
        {'name': 'bmb3 hospital', 'hospital_id': '3', 'purpose': 'nothing2'},
    ]

    return HttpResponse(json.dumps(data))

def add_prescription(request, patientid):
    data = {
        'id': patientid,
        'medicines': [
            {'name':'paracetamol', 'frequency':2, 'instructions': 'before meal'},
            {'name':'saridon', 'frequency':2, 'instructions': 'after meal'}
        ],
        'diagnostics': [
            {'name':'x ray', 'details': 'before meal'},
            {'name':'saridon', 'details': 'after meal'}
        ]
    }
    return HttpResponse(json.dumps(data))

def patient_history(request, patientid):
    data = [
        {'name': 'bmb hospital', 'hospital_id': '1', 'purpose': 'nothing'},
        {'name': 'bmb2 hospital', 'hospital_id': '2', 'purpose': 'nothing1'},
        {'name': 'bmb3 hospital', 'hospital_id': '3', 'purpose': 'nothing2'},
    ]
    return HttpResponse(json.dumps(data))

def demo(request):
    data = [
        {'name': 'bmb hospital', 'hospital_id': '1', 'purpose': 'nothing'},
        {'name': 'bmb2 hospital', 'hospital_id': '2', 'purpose': 'nothing1'},
        {'name': 'bmb3 hospital', 'hospital_id': '3', 'purpose': 'nothing2'},
    ]
    return HttpResponse(json.dumps({'status':'success'}))
