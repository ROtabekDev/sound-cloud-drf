# Generated by Django 4.1 on 2022-10-04 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, error_messages={'unique': 'Bu email mavjud.'}, max_length=254, null=True, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, error_messages={'unique': 'Bu username mavjud.'}, max_length=50, null=True, unique=True, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_links', to=settings.AUTH_USER_MODEL),
        ),
    ]
