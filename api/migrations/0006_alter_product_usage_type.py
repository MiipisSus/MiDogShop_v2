# Generated by Django 5.2.1 on 2025-06-02 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='usage_type',
            field=models.CharField(choices=[('DOG', '狗'), ('CAT', '貓'), ('GENERAL', '通用')], default='DOG', max_length=50),
        ),
    ]
