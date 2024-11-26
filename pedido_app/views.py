from django.shortcuts import render, redirect
from .models import Pedido

# Create your views here.

def inicio_vistaPedido(request):
    lospedidos=Pedido.objects.all()
    return render(request,'gestionarPedido.html',{"mispedidos":lospedidos})

def registrarPedido(request):
    id_pedido=request.POST["numidpedido"]
    fecha=request.POST["txtfecha"]
    nombre_cliente=request.POST["txtcliente"]
    producto=request.POST["txtproducto"]
    estado=request.POST["txtestado"]
    cantidad_total=request.POST["txtcantidad"]
    metodo_entrega=request.POST["txtmetodoentrega"]

    guardarpedido=Pedido.objects.create(id_pedido=id_pedido,fecha=fecha,nombre_cliente=nombre_cliente,producto=producto,estado=estado,cantidad_total=cantidad_total,metodo_entrega=metodo_entrega)

    return redirect('pedido')

def seleccionarPedido(request,id_pedido):
    pedido=Pedido.objects.get(id_pedido=id_pedido)
    return render(request,"editarPedido.html",{"mispedidos":pedido})

def editarPedido(request):
    id_pedido=request.POST["numidpedido"]
    fecha=request.POST["txtfecha"]
    nombre_cliente=request.POST["txtcliente"]
    producto=request.POST["txtproducto"]
    estado=request.POST["txtestado"]
    cantidad_total=request.POST["txtcantidad"]
    metodo_entrega=request.POST["txtmetodoentrega"]


    pedido=Pedido.objects.get(id_pedido=id_pedido)

    pedido.fecha=fecha
    pedido.nombre_cliente=nombre_cliente
    pedido.producto=producto
    pedido.estado=estado
    pedido.cantidad_total=cantidad_total
    pedido.metodo_entrega=metodo_entrega
    pedido.save()

    return redirect('pedido')

def borrarPedido(request,id_pedido):
    pedido=Pedido.objects.get(id_pedido=id_pedido)
    pedido.delete()

    return redirect('pedido')