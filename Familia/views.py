from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from Familia.forms import PersonaForm, BuscarPersonasForm, ActualizarPersonaForm, MascotaForm, ActualizarMascotaForm, BuscarMascotasForm, TrabajoForm, BuscarTrabajoForm, ActualizarTrabajoForm
from Familia.models import Persona, Mascota, Trabajo
from django.contrib import messages



# Create your views here.

# ---------------------- FAMILIA

def index(request):
    personas = Persona.objects.all()
    template = loader.get_template('Familia/lista_familiares.html')
    context = {
        'personas': personas,
    }
    return HttpResponse(template.render(context, request))


def agregar(request):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue cargada con éxito
    '''

    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            altura = form.cleaned_data['altura']
            Persona(nombre=nombre, apellido=apellido, email=email, fecha_nacimiento=fecha_nacimiento, altura=altura).save()

            messages.success(request, f'Familiar Agregado con Exito')

            return redirect('index')
            
    elif request.method == "GET":
        form = PersonaForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'Familia/form_carga.html', {'form': form})


def borrar(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue eliminada con éxito        
    '''
    if request.method == "GET":
        persona = Persona.objects.filter(id=int(identificador)).first()
        if persona:
            persona.delete()

        messages.success(request, f'Familiar Borrado con Exito')
        return redirect('index')
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def actualizar(request, identificador=''):
    '''
    TODO: implementar una vista para actualización
    '''
    if request.method == "GET":
        persona = get_object_or_404(Persona, pk=int(identificador))
        initial = {
            "id": persona.id,
            "nombre": persona.nombre, 
            "apellido": persona.apellido, 
            "email": persona.email,
            "fecha_nacimiento": persona.fecha_nacimiento.strftime("%d/%m/%Y"),
            "altura": persona.altura,
        }
    
        form_actualizar = ActualizarPersonaForm(initial=initial)
        return render(request, 'Familia/form_carga.html', {'form': form_actualizar, 'actualizar': True})
    
    elif request.method == "POST":
        form_actualizar = ActualizarPersonaForm(request.POST)
        if form_actualizar.is_valid():
            persona = get_object_or_404(Persona, pk=form_actualizar.cleaned_data['id'])
            persona.nombre = form_actualizar.cleaned_data['nombre']
            persona.apellido = form_actualizar.cleaned_data['apellido']
            persona.email = form_actualizar.cleaned_data['email']
            persona.fecha_nacimiento = form_actualizar.cleaned_data['fecha_nacimiento']
            persona.altura = form_actualizar.cleaned_data['altura']
            persona.save()

            messages.success(request, f'Familiar Actualizado con Exito')

            return redirect('index')


def buscar(request):
    
    if request.GET.get("palabra_a_buscar") and request.method == "GET":
        form_busqueda = BuscarPersonasForm(request.GET)
        if form_busqueda.is_valid():
            personas = Persona.objects.filter(nombre__icontains=request.GET.get("palabra_a_buscar"))
            return  render(request, 'Familia/lista_familiares.html', {"personas": personas, "resultados_busqueda":True})

    elif request.method == "GET":
        form_busqueda = BuscarPersonasForm()
        return render(request, 'Familia/form_busqueda.html', {"form_busqueda": form_busqueda})


# ---------------------- MASCOTAS

def index_mascotas(request):
    mascota = Mascota.objects.all()
    template = loader.get_template('Familia/lista_mascotas.html')
    context = {
        'mascotas': mascota,
    }
    return HttpResponse(template.render(context, request))


def agregar_mascota(request):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la mascota fue cargada con éxito
    '''

    if request.method == "POST":
        form = MascotaForm(request.POST)
        if form.is_valid():
            
            clase_animal = form.cleaned_data['Clase_animal']
            nombre = form.cleaned_data['nombre']
            dueño = form.cleaned_data['dueño']
            Mascota(clase_animal=clase_animal, nombre=nombre, dueño=dueño).save()

            messages.success(request, f'Mascota Agregada con Exito')

            return redirect('indexmascotas')
    elif request.method == "GET":
        form = MascotaForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")
    
    return render(request, 'Familia/form_carga_mascota.html', {'form': form})


def borrar_mascota(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la mascota fue eliminada con éxito        
    '''
    if request.method == "GET":
        mascota = Mascota.objects.filter(id=int(identificador)).first()
        if mascota:
            mascota.delete()
        messages.success(request, f'Mascota Borrada con Exito')
        return redirect('indexmascotas')
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def actualizar_mascota(request, identificador=''):
    '''
    TODO: implementar una vista para actualización
    '''
    if request.method == "GET":
        mascota = get_object_or_404(Mascota, pk=int(identificador))
        initial = {
            "id": mascota.id,
            "clase_animal": mascota.clase_animal, 
            "nombre": mascota.nombre, 
            "dueño": mascota.dueño,
            
        }
    
        form_actualizar = ActualizarMascotaForm(initial=initial)
        return render(request, 'Familia/form_carga_mascota.html', {'form': form_actualizar, 'actualizarmascota': True})
    
    elif request.method == "POST":
        form_actualizar = ActualizarMascotaForm(request.POST)
        if form_actualizar.is_valid():
            mascota = get_object_or_404(Mascota, pk=form_actualizar.cleaned_data['id'])
            mascota.clase_animal = form_actualizar.cleaned_data['Clase_animal']
            mascota.nombre = form_actualizar.cleaned_data['nombre']
            mascota.dueño = form_actualizar.cleaned_data['dueño']
            mascota.save()

            messages.success(request, f'Mascota Actualizada con Exito')

            return redirect('indexmascotas')


def buscar_mascota(request):
    
    if request.GET.get("mascota_a_buscar") and request.method == "GET":
        form_busqueda = BuscarMascotasForm(request.GET)
        if form_busqueda.is_valid():
            mascotas = Mascota.objects.filter(clase_animal__icontains=request.GET.get("mascota_a_buscar"))
            return  render(request, 'Familia/lista_mascotas.html', {"mascotas": mascotas, "resultados_busqueda":True})

    elif request.method == "GET":
        form_busqueda = BuscarMascotasForm()
        return render(request, 'Familia/form_busqueda_mascotas.html', {"form_busqueda": form_busqueda})


# ---------------------- TRABAJOS FAMILIA

def index_trabajos(request):
    trabajo = Trabajo.objects.all()
    template = loader.get_template('Familia/lista_trabajos.html')
    context = {
        'trabajos': trabajo,
    }
    return HttpResponse(template.render(context, request))


def agregar_trabajo(request):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    el trabajo fue cargada con éxito
    '''

    if request.method == "POST":
        form = TrabajoForm(request.POST)
        if form.is_valid():
            
            tipo_trabajo = form.cleaned_data['tipo_trabajo']
            trabajo = form.cleaned_data['trabajo']
            trabajador = form.cleaned_data['trabajador']
            Trabajo(tipo_trabajo=tipo_trabajo, trabajo=trabajo, trabajador=trabajador).save()

            messages.success(request, f'Trabajo Agregado con Exito')

            return redirect('indextrabajo')
    elif request.method == "GET":
        form = TrabajoForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")
    
    return render(request, 'Familia/form_carga_trabajo.html', {'form': form})


def borrar_trabajo(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    el trabajo fue eliminada con éxito        
    '''
    if request.method == "GET":
        trabajo = Trabajo.objects.filter(id=int(identificador)).first()
        if trabajo:
            trabajo.delete()
        messages.success(request, f'Trabajo Borrado con Exito')
        return redirect('indextrabajo')
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def actualizar_trabajo(request, identificador=''):
    '''
    TODO: implementar una vista para actualización
    '''
    if request.method == "GET":
        trabajo = get_object_or_404(Trabajo, pk=int(identificador))
        initial = {
            "id": trabajo.id,
            "tipo_trabajo": trabajo.tipo_trabajo, 
            "trabajo": trabajo.trabajo, 
            "trabajador": trabajo.trabajador,
            
        }
    
        form_actualizar = ActualizarTrabajoForm(initial=initial)
        return render(request, 'Familia/form_carga_trabajo.html', {'form': form_actualizar, 'actualizartrabajo': True})
    
    elif request.method == "POST":
        form_actualizar = ActualizarTrabajoForm(request.POST)
        if form_actualizar.is_valid():
            trabajo = get_object_or_404(Trabajo, pk=form_actualizar.cleaned_data['id'])
            trabajo.tipo_trabajo = form_actualizar.cleaned_data['tipo_trabajo']
            trabajo.trabajo = form_actualizar.cleaned_data['trabajo']
            trabajo.trabajador = form_actualizar.cleaned_data['trabajador']
            trabajo.save()

            messages.success(request, f'Trabajo Actualizado con Exito')

            return redirect('indextrabajo')


def buscar_trabajo(request):
    
    if request.GET.get("trabajo_a_buscar") and request.method == "GET":
        form_busqueda = BuscarTrabajoForm(request.GET)
        if form_busqueda.is_valid():
            trabajos = Trabajo.objects.filter(trabajo__icontains=request.GET.get("trabajo_a_buscar"))
            return  render(request, 'Familia/lista_trabajos.html', {"trabajos": trabajos, "resultados_busqueda":True})

    elif request.method == "GET":
        form_busqueda = BuscarTrabajoForm()
        return render(request, 'Familia/form_busqueda_trabajos.html', {"form_busqueda": form_busqueda})
