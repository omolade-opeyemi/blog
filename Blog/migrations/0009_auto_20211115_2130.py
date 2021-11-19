# Generated by Django 3.2.6 on 2021-11-15 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0008_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Title',
            new_name='Heading',
        ),
        migrations.AddField(
            model_name='post',
            name='SubHeading',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
