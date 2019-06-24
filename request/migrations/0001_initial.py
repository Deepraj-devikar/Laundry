# Generated by Django 2.2 on 2019-06-07 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rateboard', '0001_initial'),
        ('registration', '0002_auto_20190607_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_type', models.CharField(default='collecting', max_length=20)),
                ('query', models.TextField(max_length=250)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Customer')),
                ('delivery_boy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.DeliveryBoy')),
            ],
        ),
        migrations.CreateModel(
            name='RequestComplition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggest_time', models.DateTimeField()),
                ('complete_time', models.DateTimeField()),
                ('duration_late', models.DurationField(default=0)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.Request')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('item_rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rateboard.Rates')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.Request')),
            ],
        ),
    ]