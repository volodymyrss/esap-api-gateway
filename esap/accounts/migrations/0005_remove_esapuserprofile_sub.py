# Generated by Django 3.1.4 on 2021-05-28 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_esapuserprofile_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='esapuserprofile',
            name='sub',
        ),
    ]
