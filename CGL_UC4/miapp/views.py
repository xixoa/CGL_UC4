from django.shortcuts import render, HttpResponse

from miapp.models import Estudiante

# Create your views here.

def integrantes(request):
    estudiantes = ['Edgar Raul Cusi Osccorima',
                   'Carlos Eduardo Granados Pretel',
                   'Sebastian Timo Laura Antezana']
 
    return render(request,'integrantes.html', {
        'titulo':'Integrantes',
        'estudiantes': estudiantes
    })

def saludo(request):
     return render(request,'saludo.html',{
         'titulo': 'Bienvenido a todos',
         'mensaje': 'Este es un mensaje de prueba para la página web'
     })
def crear_estudiante(request):
    estudiante=Estudiante(
        codigo="1923110195",
        DNI="76177375",
        nombre="Sebastian",
        apepat="Laura",
        apemat="Antezana",
        direccion="Mz F Lote 02",
        telefono="941508479",
        estado="A"
    )
    estudiante.save()
    return HttpResponse(f"Estudiante creado: {estudiante.codigo} {estudiante.DNI} {estudiante.nombre} {estudiante.apepat} {estudiante.apemat} {estudiante.direccion} {estudiante.telefono} {estudiante.estado}")

     

    
    

    
    
