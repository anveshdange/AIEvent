# Generated by Django 3.2.12 on 2023-10-06 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIverse', '0006_remove_aiverse_sr_no_aiverse_id_alter_aiverse_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='aiverse',
            name='amount',
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
    ]
