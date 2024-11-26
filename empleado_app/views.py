from django.shortcuts import render, redirect
from .models import Empleado

# Create your views here.

def inicio_vistaEmpleado(request):
    losempleados=Empleado.objects.all()
    return render(request,'gestionarEmpleado.html',{"misempleados":losempleados})

def registrarEmpleado(request):
    id_empleado=request.POST["numidempleado"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["numtelefono"]
    correo=request.POST["txtcorreo"]
    puesto=request.POST["txtpuesto"]

    guardarempleado=Empleado.objects.create(id_empleado=id_empleado,nombre=nombre,apellido=apellido,direccion=direccion,telefono=telefono,correo=correo,puesto=puesto)

    return redirect('empleado')

def seleccionarEmpleado(request,id_empleado):
    empleado=Empleado.objects.get(id_empleado=id_empleado)
    return render(request,"editarempleado.html",{"misempleados":empleado})

def editarEmpleado(request):
    id_empleado=request.POST["numidempleado"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["numtelefono"]
    correo=request.POST["txtcorreo"]
    puesto=request.POST["txtpuesto"]


    empleado=Empleado.objects.get(id_empleado=id_empleado)

    empleado.nombre=nombre
    empleado.apellido=apellido
    empleado.direccion=direccion
    empleado.telefono=telefono
    empleado.correo=correo
    empleado.puesto=puesto
    empleado.save()

    return redirect('empleado')

def borrarEmpleado(request,id_empleado):
    empleado=Empleado.objects.get(id_empleado=id_empleado)
    empleado.delete()

    return redirect('empleado')