# Generated by Django 4.2.10 on 2024-03-04 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartTbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'part_tbl',
            },
        ),
        migrations.CreateModel(
            name='RegionTbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'region_tbl',
            },
        ),
        migrations.CreateModel(
            name='BackupTbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detailregion', models.CharField(default='null', max_length=30)),
                ('pharmacy', models.CharField(max_length=30)),
                ('businessnum', models.CharField(max_length=20)),
                ('owner', models.CharField(max_length=10)),
                ('phonenum', models.CharField(max_length=20)),
                ('contractdate', models.DateField()),
                ('expirydate', models.DateField()),
                ('category', models.CharField(default='null', max_length=20)),
                ('listprice', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('salesamount', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('profit', models.IntegerField()),
                ('part', models.ForeignKey(db_column='part_id', on_delete=django.db.models.deletion.CASCADE, to='appbackup.parttbl')),
                ('region', models.ForeignKey(db_column='region_id', on_delete=django.db.models.deletion.CASCADE, to='appbackup.regiontbl')),
            ],
            options={
                'db_table': 'backup_tbl',
            },
        ),
    ]
