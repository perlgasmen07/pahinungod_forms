# Generated by Django 4.2.11 on 2024-03-20 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partners_forms', '0003_alter_partner_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='stakeholder_category',
        ),
    ]