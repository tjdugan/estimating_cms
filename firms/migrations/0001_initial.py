# Generated by Django 3.2.13 on 2022-06-25 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Architect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('website', models.URLField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('website', models.URLField(max_length=150, null=True)),
                ('phone', models.CharField(max_length=20)),
                ('fax', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=20)),
                ('website', models.URLField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=20)),
                ('website', models.URLField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Salesman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('office_number', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=150, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firms.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=20)),
                ('officenumber', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firms.contractor')),
            ],
        ),
        migrations.CreateModel(
            name='ProductRep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('office_number', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=150, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firms.manufacturer')),
            ],
        ),
    ]