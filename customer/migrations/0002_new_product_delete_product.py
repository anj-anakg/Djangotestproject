# Generated by Django 4.2.1 on 2023-05-25 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='New_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
