# Generated by Django 4.2.3 on 2023-07-24 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0002_alter_tag_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['done', '-datetime']},
        ),
    ]
