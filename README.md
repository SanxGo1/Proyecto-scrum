# Sistema de Gestión de Inventario y Préstamos de Equipos Tecnológicos

Bienvenido al **Sistema de Gestión de Préstamos**, una herramienta diseñada para administrar de manera eficiente el inventario de equipos tecnológicos (computadores, monitores, impresoras, etc.) y controlar los préstamos y devoluciones realizados a los estudiantes.

Este sistema es interactivo, fácil de usar desde la terminal y guarda toda la información de manera automática y segura.

---

## 🚀 ¿Cómo funciona el sistema?

El objetivo principal de este programa es llevar un control exacto de **qué** equipos existen, **quién** los tiene prestados y **cuándo** son devueltos. 

Para lograrlo, el usuario simplemente debe interactuar con un menú principal numerado. El flujo lógico ideal para usar el programa es el siguiente:
1. **Registrar un equipo:** Se añade un dispositivo al inventario (ej. un computador Dell).
2. **Registrar un estudiante:** Se inscribe a la persona que va a recibir el equipo.
3. **Realizar un préstamo:** Se vincula un equipo "Disponible" con un estudiante registrado.
4. **Realizar una devolución:** El estudiante entrega el equipo, este vuelve a estar "Disponible" y se guarda un registro histórico.

---

## 📂 Descripción de los Módulos (¿Qué hace cada opción?)

El sistema está dividido en pequeños bloques o "módulos", cada uno encargado de una tarea específica para mantener el orden.

### 1. Menú Principal (`menu.py`)
Es la puerta de entrada al sistema. Aquí es donde el usuario decide qué acción quiere tomar. Muestra una lista de opciones numeradas del 1 al 6 y dirige al usuario a la función correspondiente.

### 2. Registro de Equipos (`registroequipos.py`)
Permite ingresar nuevos dispositivos al catálogo. 
* **¿Qué datos pide?** Código de serie único, tipo de dispositivo, marca, modelo y estado físico (Bueno, Óptimo o Delicado).
* **Lógica:** Si el equipo está en estado "Bueno" u "Óptimo", el sistema lo marca automáticamente como "Disponible" para préstamos.

### 3. Consulta de Equipos (`consultarequipos.py`)
Funciona como una vitrina. Al seleccionar esta opción, el sistema muestra una lista completa de todos los equipos tecnológicos registrados, detallando su serie, características y si están disponibles o prestados en ese momento.

### 4. Registro de Estudiantes (`registrar_estudiante.py`)
Antes de prestar un equipo, el sistema necesita saber a quién se lo está prestando. 
* **¿Qué datos pide?** Número de documento, nombre completo, correo electrónico y programa académico.
* **Lógica:** El sistema tiene validaciones de seguridad; por ejemplo, no permite registrar dos veces el mismo número de documento ni el mismo correo.

### 5. Sistema de Préstamos (`prestamos.py`)
Es el núcleo de la asignación. Conecta a un estudiante con un equipo tecnológico.
* **Lógica:** Verifica que el estudiante exista y que el equipo solicitado esté "Disponible". Si todo está en orden, cambia el estado del equipo a "Prestado" y genera un número de identificador único (ej. PR-1) para ese préstamo.

### 6. Sistema de Devoluciones (`devolucion.py`)
Se encarga de recibir los equipos que estaban prestados.
* **Lógica:** Busca los préstamos activos de un estudiante mediante su número de documento. Una vez que el usuario confirma qué equipo está devolviendo, el sistema vuelve a marcar el equipo como "Disponible" y guarda la fecha exacta en la que se entregó.

---

## 🗂️ ¿Dónde se guarda la información?

¡No te preocupes por perder datos! El sistema no requiere una base de datos compleja. Toda la información se guarda automáticamente en pequeños archivos de texto (con formato `.json`) dentro de una carpeta llamada **`datos`**. 

El sistema gestiona estos archivos por ti:
* **`equipos.json`**: Guarda el catálogo de dispositivos.
* **`estudiantes.json`**: Guarda el directorio de los estudiantes.
* **`prestamos.json`**: Guarda el estado actual de los equipos entregados.
* **`devoluciones.json`**: Guarda el historial de cuándo y quién entregó un equipo.

*(Nota: Gracias a los módulos internos `guardar_datos.py` y `consola.py`, el sistema crea esta carpeta sola, limpia la pantalla para que sea cómoda de leer y previene errores si algún archivo se borra accidentalmente).*

---

## 💻 Instrucciones de Uso (Para ejecutar el programa)

Para empezar a utilizar el sistema, solo necesitas tener instalado **Python** en tu computador.

1. Abre tu terminal o consola de comandos.
2. Navega hasta la carpeta donde descargaste este proyecto.
3. Escribe el siguiente comando y presiona Enter:

```bash
python menu.py
