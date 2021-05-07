# Generated by Django 3.2.2 on 2021-05-06 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('F', 'FEMALE'), ('M', 'MALE'), ('N', 'PREFER NOT TO DISCLOSE')], max_length=1),
        ),
    ]
