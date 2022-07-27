from django.shortcuts import render, HttpResponse

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
     

    
    
