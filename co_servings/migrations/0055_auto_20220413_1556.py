# Generated by Django 3.2.5 on 2022-04-13 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('co_servings', '0054_auto_20220413_1355'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='Agreement_govern',
            new_name='agreement_govern',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='Agreement_guest',
            new_name='agreement_guest',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='Agreement_investor',
            new_name='agreement_investor',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='Agreement_property_owner',
            new_name='agreement_property_owner',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='Agreement_tenant',
            new_name='agreement_tenant',
        ),
    ]
