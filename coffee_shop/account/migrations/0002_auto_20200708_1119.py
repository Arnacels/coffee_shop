# Generated by Django 3.0.8 on 2020-07-08 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referal', to='account.DiscountCard'),
        ),
    ]
