# Generated by Django 4.0.1 on 2022-03-06 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_homebanner_bannerimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homebanner',
            old_name='BannerImage',
            new_name='image',
        ),
    ]
