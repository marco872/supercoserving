# Generated by Django 3.2.5 on 2021-11-15 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('co_servings', '0037_costtrasparency_development1_guestopportunity_guestrules_hostingrules_information1_information2_ourc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
