# Generated by Django 4.2.10 on 2024-03-07 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partners_forms', '0003_alter_partner_second_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partner',
            old_name='name',
            new_name='partner_name',
        ),
    ]
