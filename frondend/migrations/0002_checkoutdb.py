# Generated by Django 4.1.3 on 2023-03-05 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frondend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkoutdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIRSTNAME', models.CharField(blank=True, max_length=30, null=True)),
                ('ADRESS', models.CharField(blank=True, max_length=30, null=True)),
                ('TOTAL', models.IntegerField(blank=True, max_length=30, null=True)),
                ('PINCODE', models.IntegerField(blank=True, max_length=30, null=True)),
                ('CARDNUMBER', models.IntegerField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
