# Sistema de Gestión de Mascotas (POO en Python)

Aplicación de consola en Python desarrollada para demostrar la implementación práctica de los pilares de la Programación Orientada a Objetos (POO). El sistema permite registrar, clasificar y visualizar diferentes tipos de mascotas (domésticas y exóticas) mediante un menú interactivo.

## Conceptos Técnicos Aplicados

Este proyecto fue estructurado aplicando los siguientes fundamentos de ingeniería de software:

* **Abstracción:** Implementación de clases abstractas usando el módulo `abc` de Python. Se definió la clase base `Mascota` de la cual derivan los demás objetos.
* **Herencia:** Creación de una jerarquía de clases donde objetos como `Gato` y `Perro` heredan atributos y métodos de las clases `Domestica` y `Mascota`.
* **Polimorfismo:** Sobrescritura del método abstracto `Habla()` en las clases hijas, permitiendo que cada objeto (ej. Gato, Perro, Tigre) tenga un comportamiento o sonido distinto al ser llamado.
* **Encapsulamiento:** Protección del estado interno de los objetos utilizando atributos privados/protegidos (ej. `self._nombre`, `self._edad`) controlados a través de métodos `getters` y `setters`.

## Estructura del Proyecto

* `pr1.py` / `pr2.py`: Scripts principales que contienen la lógica del menú, la inicialización de listas y las clases de los animales.
* `Martinez_Martinez_Nicolas_Reporte.pdf`: Documentación formal del proyecto, diagramas y análisis de código.
* `img/`: Carpeta con capturas de pantalla de las pruebas de ejecución.

## ¿Cómo ejecutarlo?

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python 3.x instalado.
3. Ejecuta el script principal desde la terminal:
   ```bash
   python pr1.py
