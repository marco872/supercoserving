# Generated by Django 3.0 on 2021-08-02 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('co_servings', '0013_project_webinvestor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='webinvestor',
        ),
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='investment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='liquidity_pool',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='webinvestor',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
