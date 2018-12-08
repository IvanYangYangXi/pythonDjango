# Generated by Django 2.1.3 on 2018-12-08 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_test', '0007_auto_20181208_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=64)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_test.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gObj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_test.UserGroup')),
                ('uObj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_test.UserInfo')),
            ],
        ),
    ]
