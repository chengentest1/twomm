# Generated by Django 2.0.7 on 2018-07-21 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_usergroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='user_type_id',
            field=models.IntegerField(choices=[(1, '超级用户'), (2, '普通用户'), (3, '普普通用户')], default=1),
        ),
    ]
