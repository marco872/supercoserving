# Generated by Django 3.2.5 on 2021-07-23 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('co_servings', '0006_auto_20210723_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='liquidity_pool',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='co_servings.project'),
        ),
    ]
