# Generated by Django 4.2.8 on 2023-12-31 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_homepage_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentinitiativeimage',
            name='write_up',
            field=models.TextField(default='A great project in alieviating the lives of little ones in ....'),
        ),
    ]