# Generated by Django 4.0.1 on 2022-03-08 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='HomeBoxSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BoxTitle', models.CharField(max_length=255)),
                ('BoxDescription', models.TextField()),
                ('BoxIcons', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HomeProductivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productivityImage', models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/')),
                ('productivityHeading', models.CharField(max_length=255)),
                ('productivityDescription', models.TextField()),
                ('productivityTestimonial', models.CharField(max_length=255)),
                ('writterImage', models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/')),
                ('writterBy', models.CharField(max_length=255)),
                ('palign', models.CharField(max_length=255)),
                ('divpAlignClass', models.CharField(max_length=255)),
            ],
        ),
    ]
