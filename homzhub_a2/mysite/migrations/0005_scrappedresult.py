# Generated by Django 3.1 on 2020-08-13 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_userrequest_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrappedResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField(default='')),
                ('Link', models.TextField(default='')),
                ('PubDate', models.TextField(default='')),
            ],
        ),
    ]
