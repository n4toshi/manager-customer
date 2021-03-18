# Generated by Django 3.1.7 on 2021-03-15 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=25)),
                ('photo', models.FileField(blank=True, null=True, upload_to='photos')),
                ('debt', models.IntegerField(default=0)),
                ('purchases', models.IntegerField(default=0)),
                ('payments', models.IntegerField(default=0)),
            ],
        ),
    ]
