# Generated by Django 4.0.4 on 2022-08-04 13:57

import contents.models
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0005_newpost_last_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='newpost',
            name='tag',
            field=models.TextField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='newpost',
            name='imgfile',
            field=imagekit.models.fields.ProcessedImageField(blank=True, default=1, upload_to=contents.models.user_path),
            preserve_default=False,
        ),
    ]
