# Generated by Django 2.2.4 on 2019-10-07 15:11

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=128)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('pet_id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('pet_name', models.CharField(default='Pets name', max_length=128)),
                ('animal_type', models.CharField(choices=[('D', 'Dog'), ('C', 'Cat')], max_length=1)),
                ('Up_for_Adoption', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('pet_profile_image', models.ImageField(upload_to='')),
                ('description', models.TextField(max_length=128)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pet_Photos',
            fields=[
                ('photo_no', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('pet_image', models.ImageField(upload_to='')),
                ('photo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petadoption.Pet')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comment_no', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('comment', models.CharField(default='Comment', max_length=128)),
                ('comment_writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('picture_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petadoption.Pet_Photos')),
            ],
        ),
        migrations.CreateModel(
            name='Adoption_requests',
            fields=[
                ('request_no', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('requester_name', models.CharField(default='Your name', max_length=128)),
                ('requester_phone_no', models.CharField(default='Yor phone no', max_length=10)),
                ('request_description', models.TextField(max_length=500)),
                ('requester_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
