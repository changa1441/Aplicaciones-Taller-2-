Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Crear una lista de comida vacía
... comida = []
... 
... # Función para agregar comida a la lista
... def agregar_comida():
...     nombre = input("Ingrese el nombre de la comida: ")
...     comida.append(nombre)
...     print(f"{nombre} ha sido agregado a la lista de comida.")
... 
... # Función para mostrar la lista de comida
... def mostrar_lista():
...     print("Lista de comida:")
...     for item in comida:
...         print(item)
... 
... # Bucle principal
... while True:
...     print("\nOpciones:")
...     print("1. Agregar comida")
...     print("2. Mostrar lista de comida")
...     print("3. Salir")
...     
...     opcion = input("Seleccione una opción: ")
...     
...     if opcion == "1":
...         agregar_comida()
...     elif opcion == "2":
...         mostrar_lista()
...     elif opcion == "3":
...         break
...     else:
...         print("Opción no válida. Intente de nuevo.")
... 
