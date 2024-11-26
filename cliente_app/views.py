from django.shortcuts import render, redirect
from .models import Cliente
 
# Create your views here.

def inicio_vistaClientes(request):
    losclientes=Cliente.objects.all()
    return render(request,'gestionarCliente.html',{"misclientes":losclientes})

def registrarCliente(request):
    id_cliente=request.POST["numidcliente"]
    nombre=request.POST["txtnombre"]
    apellidos=request.POST["txtapellido"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["numtelefono"]
    correo=request.POST["txtcorreo"]
    membresia=request.POST["txtmembresia"]

    guardarcliente=Cliente.objects.create(id_cliente=id_cliente,nombre=nombre,apellidos=apellidos,direccion=direccion,telefono=telefono,correo=correo,membresia=membresia)

    return redirect('clientes')

def seleccionarCliente(request,id_cliente):
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    return render(request,"editarCliente.html",{"misclientes":cliente})

def editarCliente(request):
    id_cliente=request.POST["numidcliente"]
    nombre=request.POST["txtnombre"]
    apellidos=request.POST["txtapellido"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["numtelefono"]
    correo=request.POST["txtcorreo"]
    membresia=request.POST["txtmembresia"]


    cliente=Cliente.objects.get(id_cliente=id_cliente)

    cliente.nombre=nombre
    cliente.apellidos=apellidos
    cliente.direccion=direccion
    cliente.telefono=telefono
    cliente.correo=correo
    cliente.membresia=membresia
    cliente.save()

    return redirect('clientes')

def borrarCliente(request,id_cliente):
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()

    return redirect('clientes')