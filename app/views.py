from django.shortcuts import render
from .models import *
from django.db.models.functions import ExtractYear
from django.db.models import Sum
import json


def index(request):
    return render(request, 'index.html', {})


def query1(request):
    rows_list = Patient.objects.by_money()
    return render(request, 'query1.html', {'rows': rows_list})


def query2(request):
    rows_list = Employee.objects.by_appointments()
    return render(request, 'query2.html', {'rows': rows_list})


def query3(request):
    patients = Patient.objects.all()
    return render(request, 'query3.html', {'patients': patients})


def app_history(request):
    selected_opt = request.GET['select_opt']
    history = Appointment.objects.app_history(selected_opt)
    return render(request, 'app_history.html', {'history': history, 'patient': selected_opt})


def treat_history(request):
    selected_opt = request.GET['select_opt']
    treatment = Appointment.objects.treat_history(selected_opt)
    return render(request, 'treat_history.html', {'treatment': treatment, 'patient': selected_opt})


def query4(request):
    patients = Patient.objects.all()
    return render(request, 'query4.html', {'patients': patients})


def query5(request):
    rows_list = Medication.objects.by_prescription()
    return render(request, 'query5.html', {'rows': rows_list})


def report1(request):
    values = [['Medical centre', 'Medical centre']]
    years = Appointment.objects.dates('start_time', 'year')
    for year in years:
        count = Appointment.objects.filter(start_time__year=ExtractYear(year)).aggregate(sum=Sum('total_cost'))
        values.append([str(year.year), count.get("sum")])

    values = json.dumps(values)
    return render(request, 'report1.html', {'values': values})


def report2(request):
    values = [['Medical centre', 'Medical centre']]
    for procedure in Procedure.objects.all():
        count = PerformedProcedures.objects.filter(procedure_id=procedure.id).aggregate(sum=Sum('amount'))
        values.append([str(procedure.name), count.get("sum")])

    values = json.dumps(values)
    return render(request, 'report2.html', {'values': values})
