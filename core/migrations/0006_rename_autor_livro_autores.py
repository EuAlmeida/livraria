# Generated by Django 4.1.2 on 2022-11-17 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_rename_preço_livro_preco"),
    ]

    operations = [
        migrations.RenameField(
            model_name="livro",
            old_name="autor",
            new_name="autores",
        ),
    ]
