# Generated by Django 3.2 on 2021-05-13 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_appointment_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='amount',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]