# Generated by Django 3.2.13 on 2022-07-02 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productrep',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='firms.manufacturer'),
        ),
        migrations.AlterField(
            model_name='projectmanager',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='firms.contractor'),
        ),
        migrations.AlterField(
            model_name='salesman',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='firms.supplier'),
        ),
    ]
