# Generated by Django 5.1.4 on 2024-12-10 22:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0004_alter_livro_editora_alter_livro_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='leitor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='biblioteca.leitor'),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='livro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='biblioteca.livro'),
        ),
    ]
