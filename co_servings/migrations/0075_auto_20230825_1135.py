# Generated by Django 3.2.5 on 2023-08-25 09:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('co_servings', '0074_auto_20230824_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='duplex',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='email',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='number',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='project',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='starting',
        ),
        migrations.RemoveField(
            model_name='liquidity',
            name='price',
        ),
        migrations.RemoveField(
            model_name='liquidity',
            name='smart_contracts',
        ),
        migrations.RemoveField(
            model_name='liquidity',
            name='status',
        ),
        migrations.RemoveField(
            model_name='liquidity',
            name='topic',
        ),
        migrations.AddField(
            model_name='liquidity',
            name='booking',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='co_servings.booking'),
        ),
        migrations.AddField(
            model_name='liquidity',
            name='percent',
            field=models.DecimalField(decimal_places=2, default=0.00, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
