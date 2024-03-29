# Generated by Django 4.2.8 on 2024-01-02 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('approved', models.BooleanField()),
            ],
        ),
    ]
