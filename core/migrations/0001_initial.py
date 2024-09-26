# Generated by Django 5.1.1 on 2024-09-26 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id_libro', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=99)),
                ('autor', models.CharField(max_length=99)),
                ('año_publicacion', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=0, max_digits=10)),
                ('copias', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'LIBROS',
            },
        ),
    ]
