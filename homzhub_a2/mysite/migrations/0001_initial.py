# Generated by Django 3.1 on 2020-08-11 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestTypeMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RequestType', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='StateMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StateName', models.TextField(default=1)),
                ('StateCode', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatusMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StatusType', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='UserRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RequestDesc', models.TextField(default='')),
                ('City', models.TextField(default='')),
                ('Pincode', models.IntegerField(default=0)),
                ('PhoneCode', models.TextField(default='')),
                ('Phone', models.IntegerField(default='')),
                ('Remark', models.TextField(default='')),
                ('RequestType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserRequest_type', to='mysite.requesttypemaster')),
                ('State', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserRequest_state', to='mysite.statemaster')),
                ('Status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserRequest_Status', to='mysite.statemaster')),
            ],
        ),
    ]