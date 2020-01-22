# Generated by Django 3.0.1 on 2020-01-11 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LabMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lab_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SemMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ShiftMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift_no', models.IntegerField()),
                ('from_time', models.TimeField()),
                ('to_time', models.TimeField()),
                ('break_from_time', models.TimeField()),
                ('break_to_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SubjectMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('short_name', models.CharField(max_length=20)),
                ('max_lab', models.IntegerField(default=0)),
                ('max_lec', models.IntegerField(default=0)),
                ('sem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general_timetable.SemMaster')),
            ],
        ),
        migrations.CreateModel(
            name='FacultyMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('alias', models.CharField(max_length=20)),
                ('hire_date', models.DateField()),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general_timetable.ShiftMaster')),
                ('subject', models.ManyToManyField(to='general_timetable.SubjectMaster')),
            ],
        ),
        migrations.CreateModel(
            name='DivisionMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('div_no', models.CharField(max_length=20)),
                ('sem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general_timetable.SemMaster')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general_timetable.ShiftMaster')),
            ],
        ),
        migrations.CreateModel(
            name='BatchMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_no', models.CharField(max_length=20)),
                ('div', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general_timetable.DivisionMaster')),
            ],
        ),
    ]