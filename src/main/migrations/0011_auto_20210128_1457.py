# Generated by Django 3.1.5 on 2021-01-28 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210128_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbacks',
            name='Image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.images'),
        ),
    ]
