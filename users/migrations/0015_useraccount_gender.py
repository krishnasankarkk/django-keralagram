# Generated by Django 4.2.7 on 2023-11-14 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_useraccount_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1),
        ),
    ]