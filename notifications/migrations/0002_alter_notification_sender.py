# Generated by Django 4.2.7 on 2024-02-06 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_useraccount_profile_pic'),
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='sender',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.useraccount'),
        ),
    ]
