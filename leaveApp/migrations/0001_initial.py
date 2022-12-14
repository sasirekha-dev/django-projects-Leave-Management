# Generated by Django 4.1.2 on 2022-10-30 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaveID', models.IntegerField()),
                ('workerID', models.IntegerField()),
                ('status', models.CharField(max_length=10)),
                ('managerID', models.IntegerField()),
                ('vacation_start_date', models.DateTimeField()),
                ('vacation_end_date', models.DateTimeField()),
            ],
        ),
    ]
