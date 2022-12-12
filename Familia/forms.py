
from django import forms
from .models import Persona

class PersonaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    email = forms.EmailField(label="Email")
    # input_format hace que se pueda ingresar la fecha con el formato latino, dia/mes/año
    fecha_nacimiento = forms.DateField(label="fecha_nacimiento", input_formats=["%d/%m/%Y"],
    #widget es para poder agregar un tip para que el usuario sepa como ingresar la fecha
    widget=forms.TextInput(attrs={'placeholder': '30/12/1995'}))
    altura = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': "1.75 m"}))


class ActualizarPersonaForm(PersonaForm):
    id = forms.IntegerField(widget = forms.HiddenInput())


class BuscarPersonasForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")



class MascotaForm(forms.Form):
    Clase_animal = forms.CharField(label="Clase de Animal", max_length=100)
    nombre = forms.CharField(label="Nombre", max_length=100)
    dueño = forms.ModelChoiceField(queryset = Persona.objects.all(),to_field_name ='nombre',empty_label="Selecciona Dueño")


class ActualizarMascotaForm(MascotaForm):
    id = forms.IntegerField(widget = forms.HiddenInput())


class BuscarMascotasForm(forms.Form):
    mascota_a_buscar = forms.CharField(label="Buscar")



class TrabajoForm(forms.Form):
    tipo_trabajo = forms.CharField(label="Tipo de Trabajo", max_length=100)
    trabajo = forms.CharField(label="Nombre", max_length=100)
    trabajador = forms.ModelChoiceField(queryset = Persona.objects.all(),to_field_name ='nombre',empty_label="Selecciona Trabajador")


class ActualizarTrabajoForm(TrabajoForm):
    id = forms.IntegerField(widget = forms.HiddenInput())


class BuscarTrabajoForm(forms.Form):
    trabajo_a_buscar = forms.CharField(label="Buscar")
    