# Generated by Django 3.2.5 on 2021-11-09 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('co_servings', '0034_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
