# Generated by Django 5.1.1 on 2024-09-23 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_recentwork_description_recentwork_technology'),
    ]

    operations = [
        migrations.AddField(
            model_name='recentwork',
            name='slug',
            field=models.SlugField(blank=True,),
        ),
    ]
