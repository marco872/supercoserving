# Generated by Django 3.2.5 on 2023-08-27 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('co_servings', '0082_auto_20230826_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]