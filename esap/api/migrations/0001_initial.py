# Generated by Django 3.0.2 on 2020-03-09 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EsapBaseObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=40)),
                ('short_description', models.CharField(max_length=40)),
                ('long_description', models.TextField(blank=True, null=True)),
                ('retrieval_description', models.TextField(blank=True, null=True)),
                ('thumbnail', models.URLField(default='https://alta.astron.nl/alta-static/unknown.jpg')),
                ('documentation_url', models.URLField(blank=True, null=True)),
                ('institute', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='ParameterMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.CharField(max_length=15)),
                ('parameters', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('esapbaseobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.EsapBaseObject')),
                ('instrument', models.CharField(max_length=30)),
            ],
            bases=('api.esapbaseobject',),
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('esapbaseobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.EsapBaseObject')),
                ('esap_service', models.CharField(default='vo', max_length=15)),
                ('equinox', models.CharField(choices=[('J2000', 'J2000'), ('ICRS', 'ICRS')], default='ICRS', max_length=10)),
                ('protocol', models.CharField(choices=[('adql', 'adql'), ('http', 'http')], max_length=15)),
                ('url', models.URLField(null=True)),
                ('parameters', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='catalogs', to='api.ParameterMapping')),
            ],
            bases=('api.esapbaseobject',),
        ),
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('esapbaseobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.EsapBaseObject')),
                ('datatype', models.CharField(max_length=30)),
                ('processing_level', models.CharField(max_length=30)),
                ('resource_name', models.CharField(blank=True, max_length=30, null=True)),
                ('select_fields', models.CharField(blank=True, default='*', max_length=100, null=True)),
                ('title_field', models.CharField(blank=True, max_length=30, null=True)),
                ('thumbnail_field', models.CharField(blank=True, max_length=30, null=True)),
                ('url_field', models.CharField(blank=True, max_length=30, null=True)),
                ('output_format', models.CharField(choices=[('list', 'list'), ('tiles', 'tiles')], default='list', max_length=10)),
                ('service_connector', models.CharField(blank=True, max_length=80, null=True)),
                ('dataset_archive', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='datasets', to='api.Archive')),
                ('dataset_catalog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='datasets', to='api.Catalog')),
            ],
            bases=('api.esapbaseobject',),
        ),
    ]