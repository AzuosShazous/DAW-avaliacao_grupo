# Generated by Django 5.1.4 on 2024-12-11 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0010_alter_autor_data_nascimento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_devolucao',
            field=models.DateField(),
        ),
    ]
