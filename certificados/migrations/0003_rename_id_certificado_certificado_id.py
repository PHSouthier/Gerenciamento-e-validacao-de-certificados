# Generated by Django 3.2.4 on 2021-07-22 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificados', '0002_auto_20210714_1556'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificado',
            old_name='id_certificado',
            new_name='id',
        ),
    ]