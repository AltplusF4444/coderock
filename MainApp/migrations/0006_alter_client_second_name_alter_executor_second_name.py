# Generated by Django 4.2 on 2023-04-10 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_alter_client_about_alter_client_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='second_name',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='executor',
            name='second_name',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
    ]
