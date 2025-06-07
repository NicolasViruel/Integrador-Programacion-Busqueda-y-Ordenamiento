import time
# --------------------------
# Algoritmo de busqueda lineal
# --------------------------
def busqueda_lineal(lista, objetivo):
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return i
    return -1

# --------------------------
# Algoritmo de busqueda binaria
# --------------------------
def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# --------------------------
# Menu para que el usuario elija
# --------------------------
def menu():
    lista = sorted([3, 7, 10, 15, 20, 25, 30, 35, 40])  # lista ordenada
    objetivo = int(input("¿Qué número querés buscar?: "))
    print("\nElegí el tipo de búsqueda:")
    print("1 - Búsqueda Lineal")
    print("2 - Búsqueda Binaria")

    opcion = input("Opción: ")

    if opcion == '1':
        inicio = time.time()
        resultado = busqueda_lineal(lista, objetivo)
        fin = time.time()
        print("Resultado:", resultado)
        print("Tiempo de ejecución (lineal):", fin - inicio, "segundos")
    elif opcion == '2':
        inicio = time.time()
        resultado = busqueda_binaria(lista, objetivo)
        fin = time.time()
        print("Resultado:", resultado)
        print("Tiempo de ejecución (binaria):", fin - inicio, "segundos")
    else:
        print("Opción inválida.")

menu()
