# Generated by Django 4.0.2 on 2022-02-08 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circuits', '0033_standardize_id_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circuit',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='circuittermination',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='circuittype',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='providernetwork',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
