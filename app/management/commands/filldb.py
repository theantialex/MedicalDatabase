from django.core.management.base import BaseCommand
from app.models import *
from random import choice
from faker import Faker
from datetime import datetime, timedelta
from django.db.models import F

fake = Faker()


class Command(BaseCommand):
    help = 'Fills database with fake data'
    specialities = [
        "Accident and emergency medicine",
        "Allergology",
        "Anaesthetics",
        "Cardiology",
        "Child psychiatry",
        "Clinical biology",
        "Clinical chemistry",
        "Clinical microbiology",
        "Clinical neurophysiology",
        "Craniofacial surgery",
        "Dermatology",
        "Endocrinology",
        "Family and General Medicine",
        "Gastroenterologic surgery",
        "Gastroenterology",
        "General Practice",
        "General surgery",
        "Geriatrics",
        "Hematology",
        "Immunology",
        "Infectious diseases",
        "Internal medicine",
        "Laboratory medicine",
        "Nephrology",
        "Neuropsychiatry",
        "Neurology",
        "Neurosurgery",
        "Nuclear medicine",
        "Obstetrics and gynaecology",
        "Occupational medicine",
        "Oncology",
        "Ophthalmology",
        "Oral and maxillofacial surgery",
        "Orthopaedics",
        "Otorhinolaryngology",
        "Paediatric surgery",
        "Paediatrics",
        "Pathology",
        "Pharmacology",
        "Physical medicine and rehabilitation",
        "Plastic surgery",
        "Podiatric surgery",
        "Preventive medicine",
        "Psychiatry",
        "Public health",
        "Radiation Oncology",
        "Radiology",
        "Respiratory medicine",
        "Rheumatology",
        "Stomatology",
        "Thoracic surgery",
        "Tropical medicine",
        "Urology",
        "Vascular surgery",
        "Venereology"
    ]

    medicine = [
        "Acetaminophen",
        "Adderall",
        "Amitriptyline",
        "Amlodipine",
        "Amoxicillin",
        "Ativan",
        "Atorvastatin",
        "Azithromycin",
        "Benzonatate",
        "Brilinta"
        "Bunavail",
        "Buprenorphine",
        "Cephalexin",
        "Ciprofloxacin",
        "Citalopram",
        "Clindamycin",
        "Clonazepam",
        "Cyclobenzaprine",
        "Cymbalta",
        "Doxycycline",
        "Dupixent",
        "Entresto",
        "Entyvio",
        "Farxiga",
        "Fentanyl",
        "Fentanyl Patch",
        "Gabapentin",
        "Gilenya",
        "Humira",
        "Hydrochlorothiazide",
        "Hydroxychloroquine",
        "Ibuprofen",
        "Imbruvica",
        "Invokana",
        "Januvia",
        "Jardiance",
        "Kevzara",
        "Lexapro",
        "Lisinopril",
        "Lofexidine",
        "Loratadine",
        "Lyrica",
        "Melatonin",
        "Meloxicam",
        "Metformin",
        "Methadone",
        "Methotrexate",
        "Metoprolol",
        "Naloxone",
        "Naltrexone",
        "Naproxen",
        "Omeprazole",
        "Onpattro",
        "Otezla",
        "Ozempic",
        "Pantoprazole",
        "Prednisone",
        "Probuphine",
        "Rybelsus",
        "Sublocade",
        "Tramadol",
        "Trazodone",
        "Viagra",
        "Wellbutrin",
        "Xanax",
        "Zubsolv"
    ]

    procedures = [
        "Biopsy test",
        "Blood test",
        "Stool test",
        "Urinalysis",
        "Cardiac stress test",
        "Electrocardiography",
        "Electrocorticography",
        "Electroencephalography",
        "Electromyography",
        "Electroneuronography",
        "Electronystagmography",
        "Electrooculography",
        "Electroretinography",
        "Endoluminal capsule monitoring",
        "Endoscopy",
        "Colonoscopy",
        "Colposcopy",
        "Cystoscopy",
        "Gastroscopy",
        "Laparoscopy",
       " Laryngoscopy",
        "Ophthalmoscopy",
        "Otoscopy",
        "Sigmoidoscopy",
        "Esophageal motility study",
        "Evoked potential",
        "Magnetoencephalography",
        "Medical imaging",
        "Angiography",
        "Aortography",
        "Cerebral angiography",
        "Coronary angiography",
        "Lymphangiography",
        "Pulmonary angiography",
        "Ventriculography",
        "Chest photofluorography",
        "Computed tomography",
        "Echocardiography",
        "Electrical impedance tomography",
        "Fluoroscopy",
        "Magnetic resonance imaging",
        "Diffuse optical imaging",
        "Diffusion tensor imaging",
        "Diffusion - weighted imaging",
        "Functional magnetic resonance imaging",
        "Positron emission tomography",
        "Radiography",
        "Scintillography",
        "SPECT",
        "Ultrasonography",
        "Contrast - enhanced ultrasound",
        "Gynecologic ultrasonography",
        "Intravascular ultrasound",
        "Obstetric ultrasonography",
        "Thermography",
        "Virtual colonoscopy",
        "Neuroimaging",
        "Posturography",
        "Insulin potentiation therapy",
        "Low - dose chemotherapy",
        "Monoclonal antibody therapy",
        "Photodynamic therapy",
        "Radiation therapy",
        "Targeted therapy",
        "Acupuncture",
        "Moxibustion",
        "Tui Na Massage",
        "Cupping / Scraping",
        "Tracheal intubation",
        "Unsealed source radiotherapy",
        "Virtual reality therapy",
        "Physical therapy / Physiotherapy",
        "Speech therapy",
        "Phototerapy",
        "Hydrotherapy",
        "Heat therapy",
        "Shock therapy"
    ]

    def add_arguments(self, parser):
        parser.add_argument('--db_size', default='small', type=str, help='The size of database data to create.')

    def fill_emloyees(self, cnt):
        employees = []
        for i in range(cnt):
            profile = fake.simple_profile()
            employees.append(Employee(
                name=profile.get('name'),
                birthday=profile.get('birthdate'),
                telephone='8' + fake.msisdn()[:10],
                email=profile.get('mail'),
                speciality=choice(self.specialities)
            ))
        Employee.objects.bulk_create(employees)

    def fill_patients(self, cnt):
        patients = []
        GENDER_CHOICES = ['F', 'M', 'N']
        for i in range(cnt):
            profile = fake.simple_profile()
            patients.append(Patient(
                name=profile.get('name'),
                birthday=profile.get('birthdate'),
                telephone='8' + fake.msisdn()[:10],
                gender=choice(GENDER_CHOICES),
                date_joined=fake.date_between(start_date=profile.get('birthdate'), end_date='today')
            ))
        Patient.objects.bulk_create(patients)

    def fill_appointments(self, cnt):
        appointments = []
        employee_ids = list(
            Employee.objects.values_list(
                'id', flat=True
            )
        )
        patient_ids = list(
            Patient.objects.values_list(
                'id', flat=True
            )
        )
        for i in range(cnt):
            patient = choice(patient_ids)
            start = fake.date_time_between(start_date=Patient.objects.get(id=patient).date_joined, end_date='now')
            appointments.append(Appointment(
                patient_id=patient,
                employee_id=choice(employee_ids),
                start_time=start,
                end_time=start + timedelta(minutes=fake.pyint(min_value=10, max_value=60)),
            ))
        Appointment.objects.bulk_create(appointments)

    def fill_medication(self, cnt):
        medications = []
        for i in range(cnt):
            medications.append(Medication(
                name=self.medicine[i],
                brand=fake.company(),
                country=fake.country(),
                cost=fake.pyint(min_value=10, max_value=30000)
            ))
        Medication.objects.bulk_create(medications)

    def fill_procedures(self, cnt):
        procedures = []
        for i in range(cnt):
            procedures.append(Procedure(
                name=self.procedures[i],
                cost=fake.pyint(min_value=100, max_value=45000)
            ))
        Procedure.objects.bulk_create(procedures)

    def fill_prescriptions(self, cnt):
        prescriptions = []
        appointment_ids = list(
            Appointment.objects.values_list(
                'id', flat=True
            )
        )
        medication_ids = list(
            Medication.objects.values_list(
                'id', flat=True
            )
        )
        for i in range(cnt):
            id = choice(appointment_ids)
            prescription = Prescription(
                appointment_id=id,
                medication_id=choice(medication_ids),
                amount=fake.pyint(min_value=1, max_value=5),
            )
            prescriptions.append(prescription)
            Appointment.objects.filter(id=id).update(total_cost=F('total_cost') +
                                                                prescription.amount * prescription.medication.cost)
        Prescription.objects.bulk_create(prescriptions)

    def fill_performed(self, cnt):
        performed = []
        appointment_ids = list(
            Appointment.objects.values_list(
                'id', flat=True
            )
        )
        procedure_ids = list(
            Procedure.objects.values_list(
                'id', flat=True
            )
        )
        for i in range(cnt):
            id = choice(appointment_ids)
            procedure = PerformedProcedures(
                appointment_id=id,
                procedure_id=choice(procedure_ids),
                amount=fake.pyint(min_value=1, max_value=5),
            )
            performed.append(procedure)
            Appointment.objects.filter(id=id).update(total_cost=F('total_cost') +
                                                                procedure.amount * procedure.procedure.cost)
        PerformedProcedures.objects.bulk_create(performed)


    def handle(self, *args, **options):
        if options['db_size'] == 'large':
            sizes = [10, 25, 45, 25, 20]
        elif options['db_size'] == 'medium':
            sizes = [10, 25, 45, 25, 20]
        else:
            sizes = [10, 25, 45, 25, 20]

        self.fill_emloyees(sizes[0])
        self.fill_patients(sizes[1])
        self.fill_appointments(sizes[2])
        self.fill_medication(len(self.medicine))
        self.fill_procedures(len(self.procedures))
        self.fill_prescriptions(sizes[3])
        self.fill_performed(sizes[4])

