Primera entrega
Desafio CoderHouse

Alumno: Vola Christian

# Proyecto Web Django con patrón MVT
-----------------------------------------

Se crearon 3 Models
- Personas (Las personas que integran la familia)
- Mascotas
- Trabajos

Tanto Mascotas como Trabajos tienen una ForeignKey que la vincula a la clase Persona (Dueño de la mascota / Trabajador)

-----------------------------------------

Por lo que el orden correcto de uso es:
1) Cargar la persona primero, es decir el familiar en cuestion
2) Luego cargar Mascota / Trabajo si es pertinente (puede no tenerlo)

Se hace de esta forma, porque en los formularios de carga de Mascotas / Trabajos posee un campo de dueño/trabajador con una lista desplegable, si no se carga primero el familiar no aparecera su nombre

------------------------------------------

En los 3 casos, cada pagina posee una funcion con sus correspondientes formularios de:
// En General :
    - AGREGAR
    - BUSCAR
// Para cada entrada tiene acciones :
    - ACTUALIZAR
    - BORRAR

En el caso de BORRAR, si se borra una persona, es decir un familiar, se borraran tambien las mascotas y trabajos asociados a esa persona. Pero si se BORRA un elemento de Mascotas/Trabajos no afectara en Familiares

------------------------------------------

Cuando se realiza una carga de datos, se actualiza, o se borra, la pagina brinda un mensaje de que la accion se realizo con exito

-----------------------------------------
GIF DE EJEMPLO DE USO:![familiares](https://user-images.githubusercontent.com/118779129/207132713-73c6cde1-1024-4258-a176-b2e73a6e6301.gif)



