# Generated by Django 3.1.5 on 2021-03-05 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_interestedservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='VStatus',
            field=models.BooleanField(default=False),
        ),
    ]
