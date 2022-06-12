# Generated by Django 3.2.7 on 2022-06-04 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('userid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=1000)),
                ('password', models.CharField(max_length=150)),
                ('role', models.IntegerField()),
                ('email', models.CharField(max_length=1000)),
                ('login_status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('teamid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('teamname', models.CharField(max_length=1000)),
                ('coachid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myLoginApp.credentials')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('playerid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='myLoginApp.credentials')),
                ('playername', models.CharField(max_length=100)),
                ('teamid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myLoginApp.teams')),
            ],
        ),
    ]
