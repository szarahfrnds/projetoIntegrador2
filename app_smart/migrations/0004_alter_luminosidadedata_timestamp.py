# Generated by Django 5.0.6 on 2024-05-27 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_smart', '0003_alter_temperaturadata_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='luminosidadedata',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
