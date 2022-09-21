# Generated by Django 3.2.6 on 2022-09-14 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_historicalproductavailability_productavailability'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproductavailability',
            name='unit',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.unit'),
        ),
        migrations.AddField(
            model_name='productavailability',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.unit'),
        ),
    ]