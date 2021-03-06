# Generated by Django 3.2.3 on 2021-10-21 18:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Community', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='commit',
            field=models.TextField(max_length=750, unique=True),
        ),
        migrations.AlterField(
            model_name='code',
            name='commit_code',
            field=models.UUIDField(blank=True, default=uuid.UUID('689f5287-87c1-43a9-ad4b-f6a157457e29')),
        ),
    ]
