# Generated by Django 3.0.4 on 2020-05-28 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_timetable', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='divisionmaster',
            name='allocated',
            field=models.IntegerField(default='0'),
        ),
    ]
