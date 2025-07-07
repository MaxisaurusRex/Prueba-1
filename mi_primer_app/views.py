from django.shortcuts import render

from .models import Familiar

from .forms import CursoForm

# Create your views here.
from django.shortcuts import HttpResponse


def inicio(request):
    return render(request, 'mi_primer_app/inicio.html')


def saludo(request):
    return HttpResponse("¡Hola, mundo!")


def saludo_con_template(request):
    return render(request, 'mi_primer_app/saludo.html')


def crear_familiar(request, nombre):
    if nombre is not None:
        # Creamos un nuevo objeto Familiar
        nuevo_familiar = Familiar(
            nombre=nombre,
            apellido="ApellidoEjemplo",
            edad=30,
            fecha_nacimiento="1993-01-01",
            parentesco="Primo"
        )
        nuevo_familiar.save()
    return render(request, "mi_primer_app/crear_familiar.html", {"nombre": nombre})


def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            # Si es un ModelForm
            form.save()
            # Si es un Form normal:
            # nombre = form.cleaned_data['nombre']
            # camada = form.cleaned_data['camada']
            # curso = Curso(nombre=nombre, camada=camada)
            # curso.save()
            return render(request, 'curso_creado.html')
    else:
        form = CursoForm()
    return render(request, 'crear_curso.html', {'form': form})


def crear_curso(request):

    return render(request, 'mi_primer_app/crear_curso.html', {})
