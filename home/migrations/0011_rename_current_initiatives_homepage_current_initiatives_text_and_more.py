# Generated by Django 4.2.8 on 2023-12-31 12:17

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_currentinitiativeimage_write_up'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='current_initiatives',
            new_name='current_initiatives_text',
        ),
        migrations.AlterField(
            model_name='currentinitiativeimage',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_initiatives', to='home.homepage'),
        ),
    ]
