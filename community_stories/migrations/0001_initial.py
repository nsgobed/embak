# Generated by Django 4.2.8 on 2024-03-06 05:59

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityStoriesIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('community_stories', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'verbose_name': 'Community Stories Page',
                'verbose_name_plural': 'Community Stories Pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]
