# Generated by Django 4.2.3 on 2023-09-20 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_myuser_image_alter_myuser_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='authentication/profile/'),
        ),
    ]
