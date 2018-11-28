# Generated by Django 2.1.2 on 2018-11-27 17:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('cedula', 'Cédula de Identidad'), ('passport', 'Pasaporte'), ('ruc', 'RUC/RISE')], default='cedula', max_length=10)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'DocumentType',
                'verbose_name_plural': 'DocumentTypes',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_id', models.CharField(max_length=10, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('second_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('second_last_name', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('direction', models.TextField()),
                ('register_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('document_type', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='people.DocumentType')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'people',
                'ordering': ['-register_at'],
                'get_latest_by': 'register_at',
            },
        ),
        migrations.CreateModel(
            name='PersonType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('natural', 'Natural'), ('juridical', 'Juridico')], default='natural', max_length=10)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'PersonType',
                'verbose_name_plural': 'PeopleType',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_id', models.PositiveIntegerField(default=0)),
                ('phone_number', models.IntegerField()),
                ('phone_type', models.CharField(choices=[('cellphone', 'Célular'), ('local', 'Local')], default='cellphone', max_length=10)),
                ('request_type', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'phone',
                'verbose_name_plural': 'phones',
            },
        ),
    ]
