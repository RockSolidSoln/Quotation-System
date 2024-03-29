# Generated by Django 4.1.4 on 2023-01-05 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=20, null=True)),
                ('customer_email', models.BigIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FinanceOfficer',
            fields=[
                ('finance_officer_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('finance_officer_name', models.CharField(max_length=20, null=True)),
                ('finance_officer_email', models.BigIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('manager_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('manager_name', models.CharField(max_length=20, null=True)),
                ('manager_email', models.BigIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='POItems',
            fields=[
                ('po_item_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('po_item_name', models.CharField(max_length=40, null=True)),
                ('po_item_quantity', models.PositiveIntegerField(default=None, null=True)),
                ('po_item_price', models.FloatField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PRItems',
            fields=[
                ('pr_item_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('pr_item_name', models.CharField(max_length=40, null=True)),
                ('pr_item_quantity', models.PositiveIntegerField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('po_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('total_price', models.FloatField(default=None, null=True)),
                ('date', models.DateField()),
                ('customer_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='project.customer')),
                ('finance_officer_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='project.financeofficer')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseRequisition',
            fields=[
                ('pr_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('customer_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='project.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('quotation_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('total_price', models.FloatField(default=None, null=True)),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=20)),
                ('customer_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='project.customer')),
                ('manager_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='project.manager')),
                ('pr_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='project.purchaserequisition')),
            ],
        ),
        migrations.CreateModel(
            name='QuotationItems',
            fields=[
                ('q_item_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('q_item_name', models.CharField(max_length=40, null=True)),
                ('q_item_quantity', models.PositiveIntegerField(default=None, null=True)),
                ('q_item_price', models.FloatField(default=None, null=True)),
                ('quotation_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='project.quotation')),
            ],
        ),
        migrations.CreateModel(
            name='Salesman',
            fields=[
                ('salesman_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('salesman_password', models.CharField(max_length=5, null=True)),
                ('salesman_email', models.BigIntegerField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddField(
            model_name='quotation',
            name='salesman_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='project.salesman'),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='quotation_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='project.quotation'),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='salesman_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='project.salesman'),
        ),
        migrations.AddField(
            model_name='pritems',
            name='pr_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='project.purchaserequisition'),
        ),
        migrations.AddField(
            model_name='poitems',
            name='po_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='project.purchaseorder'),
        ),
    ]
