# Generated by Django 3.1 on 2020-11-09 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rod', '0007_auto_20201109_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obrazek',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('zdjecie', models.BinaryField(blank=True, db_column='zdjecie')),
            ],
            options={
                'db_table': 'Obrazek',
            },
        ),
    ]