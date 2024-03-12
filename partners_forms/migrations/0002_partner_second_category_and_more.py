# Generated by Django 4.2.10 on 2024-03-06 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners_forms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='second_category',
            field=models.CharField(choices=[], max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='stakeholder_category',
            field=models.CharField(choices=[('P', 'Private'), ('G', 'Government')], max_length=64, null=True),
        ),
    ]
