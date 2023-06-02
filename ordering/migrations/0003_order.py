# Generated by Django 4.1.7 on 2023-05-15 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_alter_product_description_alter_product_name'),
        ('Registration', '0002_alter_seller_info_user_cust_info'),
        ('ordering', '0002_favourites'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('Status', models.CharField(max_length=20)),
                ('Payment_Method', models.CharField(max_length=20)),
                ('Products', models.ManyToManyField(to='seller.product')),
                ('Seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registration.seller_info')),
                ('cust_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registration.cust_info')),
            ],
        ),
    ]