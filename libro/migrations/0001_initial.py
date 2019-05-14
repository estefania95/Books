# Generated by Django 2.2.1 on 2019-05-14 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('nombreImagen', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=50)),
                ('editorial', models.CharField(max_length=100)),
                ('numeroPaginas', models.IntegerField()),
                ('anoEdicion', models.IntegerField()),
                ('sinopsis', models.TextField()),
                ('imagen', models.CharField(blank=True, max_length=200, null=True)),
                ('genero', models.ManyToManyField(to='libro.Genero')),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=100, null=True)),
                ('anoNacimiento', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('libro', models.ManyToManyField(blank=True, null=True, to='libro.Libro')),
            ],
        ),
    ]
