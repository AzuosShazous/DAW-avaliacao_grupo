# Generated by Django 5.1.4 on 2024-12-10 22:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_alter_livro_editora_alter_livro_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='editora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.editora'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.genero'),
        ),
    ]
