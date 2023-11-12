# Generated by Django 4.2.7 on 2023-11-06 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_useraccount_followers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='full_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]