# Generated by Django 3.0.8 on 2020-07-08 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200708_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountcard',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]