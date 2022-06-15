# Generated by Django 4.0.4 on 2022-05-11 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descriçao', models.TextField(blank=True, null=True)),
                ('data_evento', models.DateTimeField()),
                ('data_criaçao', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'evento',
            },
        ),
    ]
