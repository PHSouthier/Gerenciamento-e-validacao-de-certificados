# Generated by Django 3.2.4 on 2021-07-22 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificados', '0006_certificado_id_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificado',
            old_name='id_categoria',
            new_name='categoria',
        ),
    ]