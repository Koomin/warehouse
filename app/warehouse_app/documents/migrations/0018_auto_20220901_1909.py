# Generated by Django 3.2.6 on 2022-09-01 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0017_auto_20220901_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='type',
            field=models.CharField(choices=[('optima', 'Optima'), ('production', 'Production')], default='optima', max_length=11),
        ),
        migrations.AddField(
            model_name='historicaldocument',
            name='type',
            field=models.CharField(choices=[('optima', 'Optima'), ('production', 'Production')], default='optima', max_length=11),
        ),
    ]