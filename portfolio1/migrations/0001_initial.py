# Generated by Django 3.1.4 on 2021-01-18 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('photo', models.ImageField(null=True, upload_to='images/')),
                ('link', models.URLField(max_length=500, null=True)),
                ('label', models.CharField(choices=[('Web Development', 'Web Development'), ('Data Science', 'Data Science')], max_length=50, null=True)),
            ],
        ),
    ]