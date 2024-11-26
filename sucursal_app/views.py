from django.shortcuts import render, redirect
from .models import Sucursal

# Create your views here.

def inicio_vistaSucursal(request):
    lassucursales=Sucursal.objects.all()
    return render(request,'gestionarSucursal.html',{"missucursales":lassucursales})
 
def registrarSucursal(request):
    id_sucursal=request.POST["numidsucursal"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["numtelefono"]
    gerente=request.POST["txtgerente"]
    correo=request.POST["txtcorreo"]
    horario=request.POST["txthorario"]

    guardarsucursal=Sucursal.objects.create(id_sucursal=id_sucursal,nombre=nombre,direccion=direccion,telefono=telefono,gerente=gerente,correo=correo,horario=horario)

    return redirect('sucursal')

def seleccionarSucursal(request,id_sucursal):
    sucursal=Sucursal.objects.get(id_sucursal=id_sucursal)
    return render(request,"editarSucursal.html",{"missucursales":sucursal})

def editarSucursal(request):
    id_sucursal=request.POST["numidsucursal"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["numtelefono"]
    gerente=request.POST["txtgerente"]
    correo=request.POST["txtcorreo"]
    horario=request.POST["txthorario"]


    sucursal=Sucursal.objects.get(id_sucursal=id_sucursal)

    sucursal.nombre=nombre
    sucursal.direccion=direccion
    sucursal.telefono=telefono
    sucursal.gerente=gerente
    sucursal.correo=correo
    sucursal.horario=horario
    sucursal.save()

    return redirect('sucursal')

def borrarSucursal(request,id_sucursal):
    sucursal=Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursal.delete()

    return redirect('sucursal')