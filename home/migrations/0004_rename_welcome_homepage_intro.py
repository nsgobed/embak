# Generated by Django 5.0 on 2023-12-28 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_current_initiatives_homepage_overview_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='welcome',
            new_name='intro',
        ),
    ]
