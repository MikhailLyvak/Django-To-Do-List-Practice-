# Generated by Django 4.0.2 on 2023-04-03 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('done', models.BooleanField(default=False)),
                ('tags', models.ManyToManyField(related_name='tasks', to='to_do_list.Tag')),
            ],
        ),
    ]
