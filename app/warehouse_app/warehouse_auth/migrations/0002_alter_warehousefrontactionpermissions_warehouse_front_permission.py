# Generated by Django 3.2.6 on 2022-09-01 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehousefrontactionpermissions',
            name='warehouse_front_permission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='warehouse_auth.warehousefrontpermissions'),
        ),
    ]
