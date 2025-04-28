# AVL---Case-Study

**Descripción:**  
Implementacion Árbol AVL para almacenar y gestionar empleados mediante sus identificadores y fechas de antigüedad. El árbol AVL permite mantener el equilibrio automáticamente tras cada inserción o eliminación, lo que garantiza una estructura de datos eficiente para búsquedas y ordenamiento de los empleados.

Para poder visualizar los árboles se requiere la biblioteca Graphviz.

---

**Instalación de Graphviz:**  
Para poder visualizar los nodos del árbol AVL, es necesario instalar la biblioteca `graphviz`, que permite la creación de grafos y diagramas a través de su módulo `Digraph`. Esta biblioteca se puede instalar en dos pasos:  
1. Instalar Graphviz desde su [página oficial](https://graphviz.gitlab.io/download/) (asegurándose de añadir su ejecutable al `PATH` del sistema).
2. Instalar la biblioteca de Python ejecutando el siguiente comando en la terminal: pip install graphviz



**Estructura**

- `src/`: Contiene el código fuente del proyecto.
    1. `practica6.py`: Archivo principal que incluye la implementación de la clase NodoEmpleado, así como las funciones para insertar, eliminar, buscar y mostrar empleados en el árbol AVL.
    2. `menu.py`: Archivo que define un menú interactivo para utilizar las funcionalidades del árbol AVL de empleados.

---
## Funcionalidades
El programa permite las siguientes acciones:

1. Insertar empleado.
2. Eliminar empleado.
3. Buscar empleado por ID.
4. Buscar empleados por antigüedad.
5. Mostrar el árbol con Digraph de Graphviz.
6. Recorrer el árbol en orden.
7. Salir del programa.

---

## Ejecución del Programa

1. Abre una terminal.
2. Navega a la carpeta `src/`:  
   `cd ruta/a/tu/carpeta/src`
3. Ejecuta el archivo principal para iniciar el menú interactivo:  
   `python menu.py`

---

## Uso del Código

**Clase NodoEmpleado:**  
Define los nodos del árbol AVL con los atributos `id`, `fecha_de_antigüedad`, `izquierdo`, `derecho` y `altura`.

**Funciones Principales:**
- `insertar_empleado(nodo, id, fecha_de_antigüedad)`: Inserta un empleado en el árbol y ajusta la estructura para mantener el equilibrio.
- `eliminar_empleado(nodo, id)`: Elimina un empleado del árbol según su id y rebalancea el árbol.
- `buscar_empleado_por_id(nodo, id)`: Busca un empleado en el árbol por su id.
- `buscar_empleados_por_antigüedad(nodo, fecha_inicial, fecha_final)`: Muestra los empleados cuya antigüedad está dentro del rango de fechas especificado.
- `mostrar_arbol(nodo, nivel=0, prefijo="")`: Imprime en consola la estructura del árbol AVL.
- `recorrer_en_orden(nodo)`: Recorre e imprime los empleados en orden ascendente de id.

---
