# Generated by Django 4.2.7 on 2024-01-09 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_useraccount_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='bio',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
