# Generated by Django 3.2.6 on 2022-07-07 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalimport',
            name='method',
            field=models.CharField(choices=[('import_stores', 'Import stores'), ('import_documents', 'Import documents'), ('import_products', 'Import products'), ('import_documents_types', 'Import documents types'), ('import_documents_groups', 'Import documents groups'), ('full_import', 'Full import')], max_length=120),
        ),
        migrations.AlterField(
            model_name='import',
            name='method',
            field=models.CharField(choices=[('import_stores', 'Import stores'), ('import_documents', 'Import documents'), ('import_products', 'Import products'), ('import_documents_types', 'Import documents types'), ('import_documents_groups', 'Import documents groups'), ('full_import', 'Full import')], max_length=120),
        ),
    ]
