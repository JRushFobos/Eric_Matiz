# Generated by Django 4.0.4 on 2022-08-14 14:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_pizza_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='topping',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
