# Generated by Django 4.1.3 on 2023-03-04 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0002_productdb_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='admincontactdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(blank=True, max_length=100, null=True)),
                ('EMAIL', models.EmailField(blank=True, max_length=254, null=True)),
                ('SUBJECT', models.CharField(blank=True, max_length=50, null=True)),
                ('MESSAGE', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]