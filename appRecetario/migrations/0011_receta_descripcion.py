# Generated by Django 4.2.6 on 2024-11-17 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appRecetario', '0010_alter_receta_ingredientes'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]