# Generated by Django 3.2.8 on 2021-12-25 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userprofile_display_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='additional_mail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]