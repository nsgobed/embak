# Generated by Django 4.2.8 on 2024-01-02 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impact', '0004_alter_communityfeedback_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityfeedback',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
