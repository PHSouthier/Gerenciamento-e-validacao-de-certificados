# Generated by Django 3.2.4 on 2021-07-26 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificados', '0008_rename_id_usuario_certificado_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificado',
            name='imagem',
            field=models.ImageField(default='certificados/padrao.png', upload_to='certificados/'),
        ),
    ]