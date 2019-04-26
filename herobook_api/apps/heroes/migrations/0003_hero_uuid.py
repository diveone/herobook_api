# Generated by Django 2.2 on 2019-04-26 11:14

from django.db import migrations
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0002_auto_20190425_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='uuid',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22),
        ),
    ]