# Generated by Django 3.2.4 on 2021-10-06 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificados', '0015_alter_certificado_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nome',
            field=models.CharField(max_length=170),
        ),
    ]
