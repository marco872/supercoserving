# Generated by Django 3.2.5 on 2021-11-10 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('co_servings', '0035_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
