# Generated by Django 4.2.10 on 2024-03-06 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners_forms', '0002_partner_second_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='second_category',
            field=models.CharField(choices=[('1', 'NGO'), ('1', 'Company'), ('1', 'Educational Institution'), ('2', 'LGU'), ('2', 'National Government Agency'), ('2', 'Educational Institution'), ('2', 'Others')], max_length=64, null=True),
        ),
    ]