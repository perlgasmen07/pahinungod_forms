# Generated by Django 4.2.10 on 2024-03-08 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners_forms', '0017_scope_of_work_partner_scope_of_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='scope_of_work',
            field=models.ManyToManyField(blank=True, to='partners_forms.scope_of_work'),
        ),
    ]
