# Generated by Django 4.1.4 on 2023-01-11 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0013_alter_poitems_po_item_id_alter_purchaseorder_po_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='status',
            field=models.CharField(default='unclear', max_length=20),
        ),
    ]
