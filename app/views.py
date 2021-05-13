from django.shortcuts import render
from .models import *
from django.db.models import Sum
from django.core.paginator import Paginator
import json
from datetime import datetime

def get_paginator(request, obj_list, size):
    paginator = Paginator(obj_list, size)
    page = request.GET.get('page')
    return paginator.get_page(page)


def index(request):
    return render(request, 'index.html', {})


def query1(request):
    rows_list = Patient.objects.by_money()
    rows_list = get_paginator(request, rows_list, 25)
    return render(request, 'query1.html', {'rows': rows_list})


def query2(request):
    rows_list = Employee.objects.by_appointments()
    rows_list = get_paginator(request, rows_list, 25)
    return render(request, 'query2.html', {'rows': rows_list})


def query3(request):
    return render(request, 'query3.html', {})


def app_history(request):
    selected_opt = request.GET['select_opt']
    history = Appointment.objects.app_history(selected_opt)
    return render(request, 'app_history.html', {'history': history, 'patient': selected_opt})


def treat_history(request):
    selected_opt = request.GET['select_opt']
    treatment = Appointment.objects.treat_history(selected_opt)
    return render(request, 'treat_history.html', {'treatment': treatment, 'patient': selected_opt})


def query4(request):
    return render(request, 'query4.html', {})


def query5(request):
    rows_list = Medication.objects.by_prescription()
    print(Medication.objects.by_prescription().query)
    return render(request, 'query5.html', {'rows': rows_list})


def report1(request):
    values = [['Medical centre', 'Medical centre']]
    years = []
    year = datetime.now().year
    for i in range(10):
        years.append(year)
        year -= 1
    years.reverse()
    for year in years:
        count = Appointment.objects.filter(start_time__year=year).values('total_cost').aggregate(sum=Sum('total_cost'))
        values.append([str(year), count.get("sum")])
    values = json.dumps(values)
    return render(request, 'report1.html', {'values': values})

"""   
for item in Appointment.objects.values('start_time', 'total_cost'):
        if str(item.get("start_time").year) not in val_dict.keys():
            val_dict[str(item.get("start_time").year)] = item.get("total_cost")
        else:
            val_dict[str(item.get("start_time").year)] += item.get("total_cost")

    for key, value in val_dict.items():
        temp = [key, value]
        values.append(temp)
"""

def report2(request):
    values = [['Medical centre', 'Medical centre']]
    for procedure in Procedure.objects.all():
        count = PerformedProcedures.objects.filter(procedure_id=procedure.id).aggregate(sum=Sum('amount'))
        values.append([str(procedure.name), count.get("sum")])

    values = json.dumps(values)
    return render(request, 'report2.html', {'values': values})
