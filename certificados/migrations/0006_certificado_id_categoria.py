# Generated by Django 3.2.4 on 2021-07-22 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('certificados', '0005_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificado',
            name='id_categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='certificados.categoria'),
            preserve_default=False,
        ),
    ]
