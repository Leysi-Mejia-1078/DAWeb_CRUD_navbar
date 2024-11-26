from django.shortcuts import render, redirect
from .models import Proveedor

# Create your views here.

def inicio_vistaProveedor(request):
    losproveedores=Proveedor.objects.all()
    return render(request,'gestionarProveedor.html',{"misproveedores":losproveedores})

def registrarProveedor(request):
    id_proveedor=request.POST["numidproveedor"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["numtelefono"]
    correo=request.POST["txtcorreo"]
    tipo_de_producto=request.POST["txtproducto"]
    tipo_de_entrega=request.POST["txtentrega"]

    guardarproveedor=Proveedor.objects.create(id_proveedor=id_proveedor,nombre=nombre,direccion=direccion,telefono=telefono,correo=correo,tipo_de_producto=tipo_de_producto,tipo_de_entrega=tipo_de_entrega)

    return redirect('proveedor')

def seleccionarProveedor(request,id_proveedor):
    proveedor=Proveedor.objects.get(id_proveedor=id_proveedor)
    return render(request,"editarProveedor.html",{"misproveedores":proveedor})

def editarProveedor(request):
    id_proveedor=request.POST["numidproveedor"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["numtelefono"]
    correo=request.POST["txtcorreo"]
    tipo_de_producto=request.POST["txtproducto"]
    tipo_de_entrega=request.POST["txtentrega"]

    proveedor=Proveedor.objects.get(id_proveedor=id_proveedor)

    proveedor.nombre=nombre
    proveedor.direccion=direccion
    proveedor.telefono=telefono
    proveedor.correo=correo
    proveedor.tipo_de_producto=tipo_de_producto
    proveedor.tipo_de_entrega=tipo_de_entrega
    proveedor.save()

    return redirect('proveedor')

def borrarProveedor(request,id_proveedor):
    proveedor=Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.delete()

    return redirect('proveedor')