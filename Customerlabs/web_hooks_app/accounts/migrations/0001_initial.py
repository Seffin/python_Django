# Generated by Django 5.0.6 on 2024-06-13 20:03

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('account_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('account_name', models.CharField(max_length=255)),
                ('app_secret_token', models.CharField(default=uuid.uuid4, max_length=255)),
                ('website', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
