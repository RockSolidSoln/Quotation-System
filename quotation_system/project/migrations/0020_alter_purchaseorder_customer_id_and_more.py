# Generated by Django 4.1.5 on 2023-01-17 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0019_purchaserequisition_number_of_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='customer_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='project.customer'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='finance_officer_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='project.financeofficer'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='salesman_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='project.salesman'),
        ),
        migrations.AlterField(
            model_name='purchaserequisition',
            name='customer_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='project.customer'),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='customer_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='project.customer'),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='manager_id',
            field=models.ForeignKey(default='MAN0001', on_delete=django.db.models.deletion.PROTECT, to='project.manager'),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='salesman_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='project.salesman'),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='status',
            field=models.CharField(choices=[('Uncleared', 'Uncleared'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Accepted', 'Accepted'), ('Declined', 'Declined')], default='Uncleared', max_length=20),
        ),
    ]