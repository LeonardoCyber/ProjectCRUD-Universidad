from django.shortcuts import render, redirect
from . models import Curso


def home(request):
    cursos = Curso.objects.all()
    return render(request, "Gestion_cursos.html", {"cursos": cursos})

def registrar_Curso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso=Curso.objects.create(codigo=codigo,nombre=nombre,creditos=creditos)
    return redirect('/')

def eliminar_curso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect('/')

def edicion_curso(request,codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicion_curso.html", {"curso":curso})

def editar_Curso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']
    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()
    return redirect('/')
