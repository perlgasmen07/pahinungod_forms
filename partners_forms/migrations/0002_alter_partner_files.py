# Generated by Django 4.2.11 on 2024-03-20 02:33

from django.db import migrations
import partners_forms.models


class Migration(migrations.Migration):

    dependencies = [
        ('partners_forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='files',
            field=partners_forms.models.Multiple_file_field(upload_to='partner_requirements/'),
        ),
    ]