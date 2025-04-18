# Generated by Django 5.2 on 2025-04-18 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('issuer', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
                ('earn_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('skills', models.JSONField()),
                ('badge_id', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
