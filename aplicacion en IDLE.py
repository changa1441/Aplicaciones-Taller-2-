comida = []

def agregar_comida():
    nombre = input("Ingrese el nombre de la comida: ")
    comida.append(nombre)
    print(f"{nombre} ha sido agregado a la lista de comida.")

def mostrar_lista():
    print("Lista de comida:")
    for item in comida:
        print(item)

while True:
    print("\nOpciones:")
    print("1. Agregar comida")
    print("2. Mostrar lista de comida")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        agregar_comida()
    elif opcion == "2":
        mostrar_lista()
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Intente de nuevo.")

print("¡Gracias por usar el programa!")
