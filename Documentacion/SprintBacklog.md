# Sprint Backlog - Sistema de Biblioteca

Este documento contiene las historias de usuario seleccionadas para ser trabajadas en el sprint actual, con las tareas desglosadas y los criterios de aceptación correspondientes.

## Sprint Actual: 01 - Objetivo Principal: Búsqueda y Reserva de Libros

### Historia de Usuario 1: 
**Como** usuario registrado  
**Quiero** buscar libros en el catálogo  
**Para** encontrar los libros que me interesan rápidamente.

**Tareas Desglosadas**:
- Implementar búsqueda por título.
- Implementar búsqueda por autor.
- Implementar búsqueda por género.
- Mostrar resultados de la búsqueda en una lista.

**Criterios de Aceptación**:
- El sistema permite buscar por título, autor y género.
- Los resultados se muestran en una lista.
- El sistema es accesible desde distintos dispositivos.

---

### Historia de Usuario 2:
**Como** usuario registrado  
**Quiero** reservar un libro disponible  
**Para** asegurarme de que pueda retirarlo cuando esté disponible.

**Tareas Desglosadas**:
- Verificar disponibilidad del libro.
- Implementar funcionalidad de reserva.
- Mostrar confirmación de reserva.

**Criterios de Aceptación**:
- El usuario puede reservar libros disponibles.
- El sistema notifica al usuario que la reserva ha sido exitosa.
- La reserva se refleja en el estado del libro en el catálogo.

---

### Historia de Usuario 3:
**Como** administrador  
**Quiero** aprobar o rechazar las reservas de libros  
**Para** gestionar los préstamos y garantizar la disponibilidad.

**Tareas Desglosadas**:
- Crear vista para listar las reservas pendientes.
- Añadir botón para aprobar reservas.
- Añadir botón para rechazar reservas.
- Actualizar el estado del libro según la acción del administrador.

**Criterios de Aceptación**:
- El administrador puede ver una lista de todas las reservas.
- El administrador puede aprobar o rechazar una reserva.
- El sistema actualiza el estado del libro (disponible/no disponible).

---

## Tareas Técnicas:
1. Optimización de la base de datos para las consultas de búsqueda.
2. Implementación de pruebas unitarias para la funcionalidad de reserva.
3. Ajustes de diseño responsivo para la vista de administrador.

---

## Objetivo del Sprint:
El objetivo de este sprint es desarrollar y completar las funcionalidades de búsqueda y reserva de libros, así como la gestión de las reservas por parte del administrador. Al final del sprint, estas funcionalidades deben estar integradas y probadas.

