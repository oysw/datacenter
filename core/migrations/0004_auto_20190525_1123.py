# Generated by Django 2.2 on 2019-05-25 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190513_1020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='x_file',
            new_name='csv_data',
        ),
        migrations.RemoveField(
            model_name='job',
            name='y_file',
        ),
    ]