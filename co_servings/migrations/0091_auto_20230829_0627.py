# Generated by Django 3.2.5 on 2023-08-29 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('co_servings', '0090_alter_payment1_design_build_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment1',
            name='collateral_amount',
        ),
        migrations.AddField(
            model_name='payment1',
            name='collateral_lender',
            field=models.CharField(choices=[('TESTCOLL1', 'TESTCOLL1'), ('TESTCOLL2', 'TESTCOLL2')], max_length=200, null=True),
        ),
    ]
