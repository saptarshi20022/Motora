# Generated by Django 3.2.3 on 2022-06-10 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mechanic',
            fields=[
                ('mid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=255)),
                ('vehicle', models.CharField(max_length=255)),
                ('specialization', models.CharField(max_length=255)),
                ('yoe', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=255)),
                ('modelname', models.CharField(max_length=255)),
                ('serviceDescriptions', models.TextField()),
                ('bookingDate', models.DateTimeField(auto_now_add=True)),
                ('servicingDate', models.DateField()),
                ('mechanic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mechanic', to='myapp.mechanic', verbose_name='Mechanic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Book By')),
            ],
        ),
    ]
