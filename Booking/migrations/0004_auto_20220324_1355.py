# Generated by Django 3.1 on 2022-03-24 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0003_vehiclerent_bluebook_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclebook',
            name='rent_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Booking.vehiclerent'),
        ),
        migrations.AlterField(
            model_name='vehiclerent',
            name='bluebook_image',
            field=models.ImageField(upload_to='uploads/bluebooks'),
        ),
    ]
