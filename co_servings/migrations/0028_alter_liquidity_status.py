# Generated by Django 3.2.5 on 2021-08-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('co_servings', '0027_liquidity_pool_smart_contracts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liquidity',
            name='status',
            field=models.CharField(choices=[('Starting', 'Starting'), ('Filling_up', 'Filling_up'), ('Completed', 'Completed')], max_length=200, null=True),
        ),
    ]
