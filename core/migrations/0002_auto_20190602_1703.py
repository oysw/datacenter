# Generated by Django 2.2.1 on 2019-06-02 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('F', 'Finished'), ('W', 'Waiting'), ('E', 'Error'), ('P', 'Process'), ('C', 'Calculating')], default='P', max_length=10),
        ),
    ]
