# Generated by Django 5.0.3 on 2002-02-12 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_reponse_qcm_propositions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qcm',
            name='plusieurChoix',
        ),
        migrations.AlterField(
            model_name='branche',
            name='nom',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='domaine',
            name='nom',
            field=models.CharField(max_length=64),
        ),
    ]