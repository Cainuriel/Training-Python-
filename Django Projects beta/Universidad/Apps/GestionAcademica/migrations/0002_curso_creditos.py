# Generated by Django 2.1.7 on 2019-02-13 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionAcademica', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='Creditos',
            field=models.PositiveSmallIntegerField(default=25),
        ),
    ]
