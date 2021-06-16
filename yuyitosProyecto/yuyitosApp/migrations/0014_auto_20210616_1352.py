# Generated by Django 3.2.3 on 2021-06-16 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yuyitosApp', '0013_auto_20210615_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta_detalle',
            name='metodoPago',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='yuyitosApp.metodo_pago'),
        ),
        migrations.AlterField(
            model_name='metodo_pago',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
