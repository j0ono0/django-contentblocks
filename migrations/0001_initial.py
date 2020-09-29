# Generated by Django 2.2.4 on 2020-09-28 13:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('home', 'Home'), ('footer', 'Footer')], max_length=100)),
                ('content', models.TextField(default='')),
                ('weight', models.SmallIntegerField(default=0)),
                ('display_group', models.CharField(choices=[('all', 'All users'), ('anonymous', 'Anonymous users'), ('authenticated', 'Authenticated users')], default='all', max_length=50)),
                ('start_datetime', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('end_datetime', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
            options={
                'ordering': ['location', 'weight', 'start_datetime', 'end_datetime'],
            },
        ),
    ]
