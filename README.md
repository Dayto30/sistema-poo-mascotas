# Práctica 1: Operaciones Estadísticas y Sistemas de Ecuaciones en Python

Aplicación de consola en Python desarrollada para demostrar el manejo de entradas y salidas, así como la implementación de operaciones matemáticas y matriciales utilizando la biblioteca NumPy.

## Conceptos Técnicos y Bibliotecas Aplicadas

Este proyecto se divide en dos módulos principales, aplicando los siguientes conceptos:

* **Estadística Básica y Ordenamiento:** Cálculo de la media aritmética (`np.mean()`) y desviación estándar (`np.std()`) a partir de datos ingresados por el usuario.
* Implementación del algoritmo de ordenamiento burbuja sobre arreglos generados aleatoriamente mediante `random.randint()`.
* **Álgebra Lineal Computacional:** Resolución de sistemas de ecuaciones lineales 3x3 a través de representación matricial (Ax=B).
* Utiliza la función `np.linalg.solve()` para calcular las incógnitas de manera eficiente.
* **Manejo de Arreglos y Tipos de Datos:** Uso de `np.vstack()` para unir vectores y formar matrices completas.
*  Incorporación de la función `eval()` para transformar las entradas de texto del usuario en listas numéricas operables.
* **Control del Sistema:** Integración de los módulos `os` y `sys` para la limpieza de consola (`os.system('cls')`) y la finalización segura de los ciclos de ejecución (`sys.exit()`).

## Estructura del Proyecto

* `pr1.py`: Script principal enfocado en las operaciones de media aritmética, desviación estándar y el algoritmo de ordenamiento burbuja.
* `pr2.py`: Script dedicado a la resolución del sistema de ecuaciones lineales mediante álgebra de matrices.
* `Marttinez_Martinez_Nicolas_Reporte.pdf`: Documentación técnica detallada, análisis de código y capturas de prueba de las funciones operativas.
* `img/`: Directorio con capturas de pantalla de la ejecución en consola.

## Instrucciones de Ejecución

1. Asegúrate de tener Python 3.x instalado en el sistema.
2. Instala la dependencia requerida ejecutando en la terminal:
   pip install numpy
3. Para ejecutar el módulo de estadística y ordenamiento:
   python pr1.py
4. Para ejecutar el solucionador de ecuaciones matriciales:
   python pr2.py
