# Generated by Django 3.2.5 on 2023-08-28 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('co_servings', '0086_auto_20230828_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment1',
            name='booking',
            field=models.CharField(choices=[('Booking1', 'Booking1'), ('Booking2', 'Booking2'), ('Booking3', 'Booking3'), ('Booking4', 'Booking4')], max_length=200, null=True),
        ),
    ]
