# Generated by Django 4.0.2 on 2022-06-08 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=240)),
                ('url', models.CharField(max_length=240)),
                ('facilitytype', models.CharField(max_length=240)),
            ],
            options={
                'ordering': ['facilitytype', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Ida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.CharField(max_length=40)),
                ('status', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=240)),
                ('url', models.CharField(max_length=240)),
                ('ref', models.CharField(default='HEAD', max_length=240, null=True)),
                ('filepath', models.CharField(blank=True, max_length=240, null=True)),
                ('workflowtype', models.CharField(max_length=240)),
                ('keywords', models.CharField(max_length=240, null=True)),
                ('author', models.CharField(max_length=240, null=True)),
                ('runtimePlatform', models.CharField(max_length=240, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.PositiveIntegerField()),
                ('dataset', models.PositiveIntegerField()),
                ('datatype', models.CharField(max_length=240)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ida.facility')),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ida.workflow')),
            ],
        ),
    ]
