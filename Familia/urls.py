from django.urls import path
from Familia import views


urlpatterns = [
    path('', views.index, name="index"),
    path('agregar/', views.agregar, name="agregar"),
    path('borrar/<identificador>', views.borrar, name="borrar"),
    path('actualizar/', views.actualizar, name="actualizar_action"),
    path('actualizar/<identificador>', views.actualizar, name="actualizar"),
    path('buscar/', views.buscar, name="buscar"),

    path('mascotas/', views.index_mascotas, name="indexmascotas"),
    path('agregarmascota/', views.agregar_mascota, name="agregarmascota"),
    path('borrarmascota/<identificador>', views.borrar_mascota, name="borrarmascota"),
    path('actualizarmascota/', views.actualizar_mascota, name="actualizar_action_mascota"),
    path('actualizarmascota/<identificador>', views.actualizar_mascota, name="actualizarmascota"),
    path('buscarmascota/', views.buscar_mascota, name="buscarmascota"),

    path('trabajos/', views.index_trabajos, name="indextrabajo"),
    path('agregartrabajo/', views.agregar_trabajo, name="agregartrabajo"),
    path('borrartrabajo/<identificador>', views.borrar_trabajo, name="borrartrabajo"),
    path('actualizartrabajo/', views.actualizar_trabajo, name="actualizar_action_trabajo"),
    path('actualizartrabajo/<identificador>', views.actualizar_trabajo, name="actualizartrabajo"),
    path('buscartrabajo/', views.buscar_trabajo, name="buscartrabajo"),
]