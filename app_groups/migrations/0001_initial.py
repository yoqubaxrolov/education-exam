# Generated by Django 5.1.6 on 2025-03-09 07:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField(null=True)),
                ('students', models.ManyToManyField(limit_choices_to={'role': 'student'}, related_name='students', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(limit_choices_to={'role': 'teacher'}, on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
            },
        ),
    ]
