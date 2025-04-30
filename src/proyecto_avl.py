from graphviz import Digraph # type: ignore #importamos Digraph de graphviz para poder imprimir los nodos

# Creamos la clase en la cual se va a representar a cada empleado en el arbol
class NodoEmpleado:
    def __init__(self, id, fecha_de_antigüedad):
        self.id = id
        self.fecha_de_antigüedad = fecha_de_antigüedad
        self.izquierdo = None
        self.derecho = None
        self.altura = 1 # si inicializamos la altura en 1 podemos calcular el balance de las hojas.

# Altura y balanceo
def obtener_altura(nodo):
    if nodo is None:
        return 0
    return nodo.altura # Almacenaremos en cada nodo su respectiva altura que será modificada al insertar y eliminar

def calcular_balance(nodo):
    if nodo is None:
        return 0
    return obtener_altura(nodo.derecho) - obtener_altura(nodo.izquierdo)

def actualizar_altura(nodo):
    nodo.altura= 1 + max(obtener_altura(nodo.derecho), obtener_altura(nodo.izquierdo))

# Rotaciones
def rotacion_derecha(nodo):
    if nodo is None or nodo.izquierdo is None:
        return nodo  # No se puede realizar rotación si no hay hijo izquierdo

    n_temp0 = nodo.izquierdo
    n_temp1 = n_temp0.derecho if n_temp0 is not None else None

    # Realizamos la rotación
    n_temp0.derecho = nodo
    nodo.izquierdo = n_temp1

    # Actualizamos las alturas
    nodo.altura = 1 + max(obtener_altura(nodo.izquierdo), obtener_altura(nodo.derecho))
    n_temp0.altura = 1 + max(obtener_altura(n_temp0.izquierdo), obtener_altura(n_temp0.derecho))

    # Retornamos la nueva raíz
    return n_temp0

def rotacion_izquierda(n_temp0):
    if n_temp0 is None or n_temp0.derecho is None:
        return n_temp0  # No se puede realizar rotación si no hay hijo derecho

    nodo = n_temp0.derecho
    n_temp1 = nodo.izquierdo if nodo is not None else None

    # Realizamos la rotación
    nodo.izquierdo = n_temp0
    n_temp0.derecho = n_temp1

    # Actualizamos las alturas
    n_temp0.altura = 1 + max(obtener_altura(n_temp0.izquierdo), obtener_altura(n_temp0.derecho))
    nodo.altura = 1 + max(obtener_altura(nodo.izquierdo), obtener_altura(nodo.derecho))

    # Retornamos la nueva raíz
    return nodo

# Balanceo
def balancear(nodo):
    # Calculamos el factor de balance para ver si el nodo necesita balancearse
    balance = calcular_balance(nodo)

    # Caso de rotación derecha (Simple derecha)
    if balance > 1 and calcular_balance(nodo.izquierdo) >= 0:
        return rotacion_derecha(nodo)

    # Caso de rotación izquierda-derecha (Doble derecha)
    if balance > 1 and calcular_balance(nodo.izquierdo) < 0:
        nodo.izquierdo = rotacion_izquierda(nodo.izquierdo)
        return rotacion_derecha(nodo)

    # Caso de rotación izquierda (Simple izquierda)
    if balance < -1 and calcular_balance(nodo.derecho) <= 0:
        return rotacion_izquierda(nodo)

    # Caso de rotación derecha-izquierda (domble izquierda)
    if balance < -1 and calcular_balance(nodo.derecho) > 0:
        nodo.derecho = rotacion_derecha(nodo.derecho)
        return rotacion_izquierda(nodo)

    # Si el nodo está balanceado, no hacemos nada
    return nodo

# Inserción de un empleado en el árbol de jerarquía recursivamente, al ser recursiva podemos actualizar las alturas en cada paso recursivo.
def insertar_empleado(arbol, nuevo_id, nueva_fecha):
    # Si el árbol está vacío, creamos un nuevo nodo y lo retornamos
    if arbol is None:
        print(f"Insertando nodo: ID = {id}, Fecha de Antigüedad = {nueva_fecha}")
        return NodoEmpleado(nuevo_id, nueva_fecha)

    # Realizamos la inserción recursivamente
    if nuevo_id < arbol.id:
        arbol.izquierdo = insertar_empleado(arbol.izquierdo, nuevo_id, nueva_fecha)
    else:
        arbol.derecho = insertar_empleado(arbol.derecho, nuevo_id, nueva_fecha)

    # Actualizamos la altura del nodo actual
    actualizar_altura(arbol)

    # Balanceamos el nodo actual si es necesario
    return balancear(arbol)  # Aseguramos devolver siempre la raíz del subárbol balanceado

# Eliminación usando el ID como criterio
def eliminar_empleado(arbol, id_eliminar):
    # Caso base: si el árbol está vacío
    if arbol is None:
        print(f"ID {id_eliminar} no encontrado.")
        return None

    # Si el ID a eliminar es menor que el ID del nodo actual, se busca en el subárbol izquierdo
    if id_eliminar < arbol.id:
        arbol.izquierdo = eliminar_empleado(arbol.izquierdo, id_eliminar)

    # Si el ID a eliminar es mayor que el ID del nodo actual, se busca en el subárbol derecho
    elif id_eliminar > arbol.id:
        arbol.derecho = eliminar_empleado(arbol.derecho, id_eliminar)

    # Si el ID coincide con el del nodo actual, ya encontramos el nodo a eliminar
    else:
        print(f"Eliminando nodo: ID = {arbol.id}")
        # Caso 1: el nodo a eliminar no tiene hijo izquierdo (se conecta al subárbol derecho)
        if arbol.izquierdo is None:
            return arbol.derecho
        # Caso 2: el nodo a eliminar no tiene hijo derecho (se conecta al subárbol izquierdo)
        elif arbol.derecho is None:
            return arbol.izquierdo

        # Caso 3: el nodo tiene ambos hijos (izquierdo y derecho)
        nodo_min = arbol.derecho # Para mantener el orden del árbol, buscamos el nodo más chico en el subárbol derecho
        while nodo_min.izquierdo is not None:
            nodo_min = nodo_min.izquierdo
        arbol.id = nodo_min.id
        arbol.fecha_de_antigüedad = nodo_min.fecha_de_antigüedad
        arbol.derecho = eliminar_empleado(arbol.derecho, nodo_min.id)

    return arbol

# Búsqueda de un empleado en el árbol
def buscar_empleado(arbol, id_buscar):
    nodo_temp = arbol

    # Recorremos el árbol en busca del id deseado
    while nodo_temp is not None:
        if id_buscar < nodo_temp.id:
            nodo_temp = nodo_temp.izquierdo
        elif id_buscar > nodo_temp.id:
            nodo_temp = nodo_temp.derecho
        else:
            return nodo_temp
    return None

def obtener_fecha_antiguedad(arbol):
    while True:
        try:
            año = int(input("Ingresa el año (YYYY): "))
            mes = int(input("Ingresa el mes (MM): "))
            dia = int(input("Ingresa el día (DD): "))

            # Formateamos la fecha en el formato "YYYY/MM/DD" para almacenarla
            fecha_formateada = f"{año:04d}/{mes:02d}/{dia:02d}"

            # Generamos el ID inicial basado en la fecha en formato "YYYYMMDD"
            base_id = int(f"{año:04d}{mes:02d}{dia:02d}")
            id_unico = base_id
            count = 0

            # Verifica si el ID ya existe en el árbol, y si es así, agrega un sufijo único
            while buscar_empleado(arbol, id_unico) is not None:
                count += 1
                id_unico = int(f"{base_id}{count}")

            # Retorna la fecha formateada y el ID único generado
            return fecha_formateada, id_unico
        except ValueError:
            print("Error: Ingresa valores numéricos válidos para la fecha.")

#imprimir el arbol
def mostrar_arbol(arbol):
    dot = Digraph()
    dot.attr(rankdir='TB')  # Organiza el árbol de arriba hacia abajo (Top-Bottom)
    dot.attr('node', shape='circle')  # Usa nodos circulares para el árbol

    def agregar_nodos_dot(nodo):
        if nodo is not None:
            # Agrega el nodo actual con el ID y la fecha de antigüedad en la etiqueta
            dot.node(str(nodo.id), f"{nodo.id}\nAnt: {nodo.fecha_de_antigüedad}")

            # Agrega la conexión con el hijo izquierdo
            if nodo.izquierdo is not None:
                dot.edge(str(nodo.id), str(nodo.izquierdo.id))
                agregar_nodos_dot(nodo.izquierdo)

            # Agrega la conexión con el hijo derecho
            if nodo.derecho is not None:
                dot.edge(str(nodo.id), str(nodo.derecho.id))
                agregar_nodos_dot(nodo.derecho)

    # Llama a la función recursiva para llenar el gráfico
    agregar_nodos_dot(arbol)

    # Renderiza y muestra el gráfico
    dot.render("arbol_avl", format="png", view=True)

def menu():
    arbol = None
    while True:
        print("\n--- Menú Árbol AVL de Empleados ---")
        print("1. Insertar empleado")
        print("2. Eliminar empleado")
        print("3. Buscar empleado por ID")
        print("4. Buscar empleados por antigüedad")
        print("5. Mostrar árbol")
        print("6. Recorrer en orden")
        print("7. Contar empleados")
        print("8. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            # Solicitar la fecha de antigüedad en tres partes y generar un ID único basado en la fecha
            nueva_fecha, nuevo_id = obtener_fecha_antiguedad(arbol)
            arbol = insertar_empleado(arbol, nuevo_id, nueva_fecha)
            print(f"Empleado insertado con ID {nuevo_id} y fecha de antigüedad {nueva_fecha}.")

        elif opcion == '2':
            id_eliminar = int(input("Ingresa el ID del empleado a eliminar: "))
            arbol = eliminar_empleado(arbol, id_eliminar)
            print("Empleado eliminado correctamente.")

        elif opcion == '3':
            id_buscar = int(input("Ingresa el ID del empleado a buscar: "))
            empleado = buscar_empleado(arbol, id_buscar)
            if empleado:
                print(f"Empleado encontrado: ID = {empleado.id}, Fecha = {empleado.fecha_de_antigüedad}")
            else:
                print("Empleado no encontrado")

        elif opcion == '4':
            fecha_buscar = input("Ingresa la fecha de antigüedad a buscar (YYYY-MM-DD): ")
            resultados = buscar_por_antigüedad(arbol, fecha_buscar)
            if resultados:
                print(f"Empleados con fecha de antigüedad {fecha_buscar}:")
                for id, fecha in resultados:
                    print(f"ID: {id}, Fecha de Antigüedad: {fecha}")
            else:
                print("No se encontraron empleados con esa fecha de antigüedad.")

        elif opcion == '5':
            print("\n--- Estructura del Árbol AVL ---")
            mostrar_arbol(arbol)

        elif opcion == '6':
            print("Recorrido en orden:")
            recorrer_en_orden(arbol)

        elif opcion == '7':
            # Llamada a la función contar_empleados para obtener el total de empleados
            total_empleados = contar_empleados(arbol)
            print(f"Total de empleados en el árbol: {total_empleados}")

        elif opcion == '8':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

"""### Operaciones extras"""

# Recorrido en orden: muestra todos los empleados en orden de antigüedad
def recorrer_en_orden(arbol):
    if arbol is not None:
        # Se recorre el subárbol izquierdo primero
        recorrer_en_orden(arbol.izquierdo)
        # Imprimimos el ID y fecha de antigüedad del nodo actual
        print(f"ID: {arbol.id}, Fecha de Antigüedad: {arbol.fecha_de_antigüedad}")
        # Luego se recorre el subárbol derecho
        recorrer_en_orden(arbol.derecho)

# Contar el total de empleados en el árbol
def contar_empleados(arbol):
    if arbol is None:
        # Caso base: Si el nodo es nulo, no hay empleado
        return 0
    # Contamos el nodo actual más los nodos en el subárbol izquierdo y derecho
    return 1 + contar_empleados(arbol.izquierdo) + contar_empleados(arbol.derecho)

# Buscar empleados por fecha de antigüedad específica
def buscar_por_antigüedad(arbol, fecha_buscar):
    resultados = []
    # Función auxiliar para recorrer el árbol y buscar en cada nodo
    def buscar_en_nodo(nodo, fecha_buscar):
        if nodo is not None:
            # Primero, buscamos en el subárbol izquierdo
            buscar_en_nodo(nodo.izquierdo, fecha_buscar)
            # Si la fecha coincide, agregamos el empleado a los resultados
            if nodo.fecha_de_antigüedad == fecha_buscar:
                resultados.append((nodo.id, nodo.fecha_de_antigüedad))
            # Luego, buscamos en el subárbol derecho
            buscar_en_nodo(nodo.derecho, fecha_buscar)
    # Iniciamos la búsqueda desde el nodo raíz
    buscar_en_nodo(arbol, fecha_buscar)
    return resultados

# Ejemplo
# Creamos el árbol, insertanod a algunos empleados con diferentes fechas de antigüedad
arbol = None
arbol = insertar_empleado(arbol, 1, "2021/05/10")
arbol = insertar_empleado(arbol, 2, "2019/03/25")
arbol = insertar_empleado(arbol, 3, "2020/11/30")
arbol = insertar_empleado(arbol, 4, "2018/07/15")
arbol = insertar_empleado(arbol, 5, "2022/01/01")

print("________________________________________________________________________\n")

# Prueba de las funciones implementadas
print("\nRecorrido en orden:")
recorrer_en_orden(arbol)  # Imprime cada empleado en orden de antigüedad

print("\nTotal de empleados:", contar_empleados(arbol))  # Cuenta total de empleados

# Buscar empleados con una fecha específica de antigüedad
fecha_deseada = "2020/11/30"  # Fecha de antigüedad a buscar
resultados = buscar_por_antigüedad(arbol, fecha_deseada)
print(f"\nEmpleados con fecha de antigüedad {fecha_deseada}:")
for empleado in resultados:
    print(f"ID: {empleado[0]}, Fecha de Antigüedad: {empleado[1]}\n")

print("________________________________________________________________________\n")

# Eliminar un empleado por su ID
id_a_eliminar = 3
arbol = eliminar_empleado(arbol, id_a_eliminar)

# Mostramos el estado del árbol después de la eliminación
print("\nRecorrido en orden después de eliminar el empleado con ID 3:")
recorrer_en_orden(arbol)

print("\nTotal de empleados después de la eliminación:", contar_empleados(arbol))

menu()