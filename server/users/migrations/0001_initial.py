# Generated by Django 4.2.5 on 2023-10-08 15:55

from django.db import migrations, models
import users.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Username')),
                ('first_name', models.CharField(blank=True, max_length=50, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=50, verbose_name='last name')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='when updated')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=(models.Model, PermissionError),
            managers=[
                ('objects', users.managers.UserManager()),
            ],
        ),
    ]