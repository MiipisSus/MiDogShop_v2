# Generated by Django 5.2.1 on 2025-06-02 09:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_product_usage_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='api.category'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PENDING', '待付款'), ('PAID', '已付款'), ('SHIPPED', '已出貨'), ('ARRIVED', '已到貨'), ('COMPLETED', '已完成'), ('CANCELED', '已取消')], default='PENDING', max_length=50),
        ),
    ]
