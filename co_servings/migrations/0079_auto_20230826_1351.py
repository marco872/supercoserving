# Generated by Django 3.2.5 on 2023-08-26 11:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('co_servings', '0078_liquidity_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='liquidity',
            name='collateral_amount',
            field=models.DecimalField(decimal_places=2, default=django.utils.timezone.now, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='liquidity',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]