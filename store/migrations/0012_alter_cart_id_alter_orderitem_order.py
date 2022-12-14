# Generated by Django 4.1 on 2022-10-17 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_customer_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='store.order'),
        ),
    ]
