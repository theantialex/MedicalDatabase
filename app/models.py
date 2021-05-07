from django.db import models
from django.db.models import Sum, Count


class PatientManager(models.Manager):
    def by_money(self):
        return self.prefetch_related('appointments').annotate(money=Sum('appointments__total_cost')).order_by('-money')


class EmployeeManager(models.Manager):
    def by_appointments(self):
        return self.prefetch_related('appointments').annotate(count=Count('appointments')).order_by('-count')


class MedicationManager(models.Manager):
    def by_prescription(self):
        return self.prefetch_related('prescriptions').annotate(count=Sum('prescriptions__amount'),
                                                               app=Count('prescriptions')).order_by('-count')


class AppointmentManager(models.Manager):
    def app_history(self, name):
        return self.prefetch_related('patient').filter(patient__name=name)

    def treat_history(self, name):
        return self.prefetch_related('prescriptions', 'patient', 'performed').filter(patient__name=name)


class Employee(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    telephone = models.CharField(max_length=10)
    email = models.EmailField(blank=True)
    speciality = models.CharField(max_length=255)
    objects = EmployeeManager()

    def __str__(self):
        return self.name


class Patient(models.Model):
    GENDER_CHOICES = (('F', 'FEMALE'), ('M', 'MALE'), ('N', 'PREFER NOT TO DISCLOSE'))

    name = models.CharField(max_length=100)
    birthday = models.DateField()
    telephone = models.CharField(max_length=10)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    date_joined = models.DateField()
    objects = PatientManager()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    employee = models.ForeignKey('Employee', related_name='appointments', on_delete=models.CASCADE)
    patient = models.ForeignKey('Patient', related_name='appointments', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_cost = models.IntegerField(default=0)
    objects = AppointmentManager()

    def __str__(self):
        return str(self.start_time) + ' Doc: ' + self.employee.name + ' Pat: ' + self.patient.name


class Medication(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    cost = models.IntegerField()
    objects = MedicationManager()

    def __str__(self):
        return self.name


class Procedure(models.Model):
    name = models.CharField(max_length=255)
    cost = models.IntegerField()

    def __str__(self):
        return self.name


class Prescription(models.Model):
    appointment = models.ForeignKey('Appointment', related_name='prescriptions',on_delete=models.CASCADE)
    medication = models.ForeignKey('Medication', related_name='prescriptions', on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return str(self.amount) + ' ' + self.medication.name


class PerformedProcedures(models.Model):
    appointment = models.ForeignKey('Appointment', related_name='performed', on_delete=models.CASCADE)
    procedure = models.ForeignKey('Procedure', related_name='performed', on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return str(self.amount) + ' ' + self.procedure.name
