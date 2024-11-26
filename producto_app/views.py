from django.shortcuts import render, redirect
from .models import Producto

# Create your views here.

def inicio_vistaProducto(request):
    losproductos=Producto.objects.all()
    return render(request,'gestionarProducto.html',{"misproductos":losproductos})

def registrarProducto(request):
    id_producto=request.POST["numidproducto"]
    nombre=request.POST["txtnombre"]
    tipo=request.POST["txttipo"]
    material=request.POST["txtmaterial"]
    peso=request.POST["numpeso"]
    precio=request.POST["numprecio"]
    tamano=request.POST["txttamano"]

    guardarproducto=Producto.objects.create(id_producto=id_producto,nombre=nombre,tipo=tipo,material=material,peso=peso,precio=precio,tamano=tamano)

    return redirect('producto')

def seleccionarProducto(request,id_producto):
    producto=Producto.objects.get(id_producto=id_producto)
    return render(request,"editarProducto.html",{"misproductos":producto})

def editarProducto(request):
    id_producto=request.POST["numidproducto"]
    nombre=request.POST["txtnombre"]
    tipo=request.POST["txttipo"]
    material=request.POST["txtmaterial"]
    peso=request.POST["numpeso"]
    precio=request.POST["numprecio"]
    tamano=request.POST["txttamano"]


    producto=Producto.objects.get(id_producto=id_producto)
 
    producto.nombre=nombre
    producto.tipo=tipo
    producto.material=material
    producto.peso=peso
    producto.precio=precio
    producto.tamano=tamano
    producto.save()

    return redirect('producto')

def borrarProducto(request,id_producto):
    producto=Producto.objects.get(id_producto=id_producto)
    producto.delete()

    return redirect('producto')