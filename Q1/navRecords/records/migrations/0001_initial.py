# Generated by Django 3.2.4 on 2021-06-15 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=20, verbose_name='Plaka')),
            ],
        ),
        migrations.CreateModel(
            name='NavigationRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(default=0, verbose_name='enlem')),
                ('longitude', models.FloatField(default=0, verbose_name='boylam')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Son görülme tarihi')),
                ('vehicle', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='Vehicle', to='records.vehicle', verbose_name='Plaka')),
            ],
        ),
    ]
