# Generated by Django 3.2 on 2021-04-29 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RMS', '0004_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='Food/'),
        ),
    ]
