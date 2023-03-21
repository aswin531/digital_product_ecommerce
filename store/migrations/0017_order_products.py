# Generated by Django 4.0.5 on 2023-03-21 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_remove_orderitem_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='orders', to='store.product'),
        ),
    ]
