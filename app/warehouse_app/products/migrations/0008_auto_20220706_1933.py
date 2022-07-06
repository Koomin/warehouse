# Generated by Django 3.2.6 on 2022-07-06 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20220706_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproduct',
            name='retail_value',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=12),
        ),
        migrations.AddField(
            model_name='product',
            name='retail_value',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=12),
        ),
    ]
