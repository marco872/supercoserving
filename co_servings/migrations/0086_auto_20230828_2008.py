# Generated by Django 3.2.5 on 2023-08-28 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('co_servings', '0085_auto_20230827_1711'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment1',
            old_name='name',
            new_name='Design_Build_Project',
        ),
        migrations.AddField(
            model_name='payment1',
            name='collateral_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='payment1',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='payment1',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
