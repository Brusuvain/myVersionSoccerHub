# Generated by Django 4.0.5 on 2022-06-13 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myLoginApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='coachid',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='myLoginApp.credentials'),
        ),
    ]
