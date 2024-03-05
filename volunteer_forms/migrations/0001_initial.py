# Generated by Django 4.2.10 on 2024-03-05 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beneficiaries', models.CharField(max_length=50)),
                ('relation', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prcLicense', models.CharField(max_length=7)),
                ('dept', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('officeAdd', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('workSched', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idNum', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('college', models.CharField(max_length=50)),
                ('yearLvl', models.CharField(choices=[('1', '1st Year'), ('2', '2nd Year'), ('3', '3rd Year'), ('4', '4th Year'), ('5', '5th Year')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=13)),
                ('telephone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('birthdate', models.DateField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('civilStatus', models.CharField(choices=[('S', 'Single'), ('M', 'Married')], max_length=1)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other/Will not disclose')], max_length=1)),
                ('bloodType', models.CharField(max_length=3)),
                ('religion', models.CharField(max_length=50)),
                ('healthConditions', models.CharField(max_length=50)),
                ('skillsHobbies', models.CharField(max_length=50)),
                ('foodRestrictions', models.CharField(max_length=50)),
                ('constituentUnit', models.CharField(max_length=50)),
                ('specification', models.CharField(max_length=50)),
                ('occupation', models.CharField(choices=[('PY', 'Physician'), ('NR', 'Nurse'), ('PH', 'Pharmacist'), ('DE', 'Dentist'), ('EN', 'ENT'), ('TE', 'Teacher'), ('OT', 'Other')], max_length=2)),
                ('insurance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insurance', to='volunteer_forms.insurance')),
                ('license', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='license', to='volunteer_forms.license')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='volunteer_forms.student')),
            ],
        ),
    ]
