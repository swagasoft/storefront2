# Generated by Django 4.1 on 2022-10-22 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_cart_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together=set(),
        ),
    ]