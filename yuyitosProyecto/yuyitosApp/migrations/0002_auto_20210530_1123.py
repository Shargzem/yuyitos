# Generated by Django 3.2.3 on 2021-05-30 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yuyitosApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleta',
            name='idBoleta',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='idCliente',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='fiado',
            name='idFiado',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='metodo_pago',
            name='idMetodoPago',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='idPedido',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pedido_producto',
            name='idPedidoProducto',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='producto',
            name='idProducto',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tipo_producto',
            name='idTipoProducto',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='venta_detalle',
            name='idVentaDetalle',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
