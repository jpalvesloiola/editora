# Generated by Django 5.1.7 on 2025-03-31 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_alter_livro_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='isbn',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='ISBN'),
        ),
    ]
