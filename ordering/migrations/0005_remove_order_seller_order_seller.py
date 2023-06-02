# Generated by Django 4.1.7 on 2023-05-15 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0002_alter_seller_info_user_cust_info'),
        ('ordering', '0004_alter_order_cust_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Seller',
        ),
        migrations.AddField(
            model_name='order',
            name='Seller',
            field=models.ManyToManyField(to='Registration.seller_info'),
        ),
    ]