# Generated by Django 4.2 on 2023-04-08 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0003_remove_artifact_text_artifact_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artifact',
            name='Description',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
