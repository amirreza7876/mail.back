# Generated by Django 3.2.9 on 2022-04-06 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='friends',
            field=models.ManyToManyField(related_name='_Users_wallet_friends_+', to='Users.Wallet'),
        ),
    ]
