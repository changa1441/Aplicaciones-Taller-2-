# Importamos las librerías necesarias
import random

# Creamos una lista de preguntas
preguntas = ["¿Cuál es tu color favorito?", "¿Cuál es tu animal favorito?", "¿Cuál es tu libro favorito?"]

# Creamos una lista de respuestas
respuestas = ["Rojo", "Perro", "Harry Potter"]

# Generamos una encuesta aleatoria
encuesta = []
for i in range(len(preguntas)):
    encuesta.append((preguntas[i], respuestas[random.randint(0, len(respuestas) - 1)]))

# Imprimimos la encuesta
print("Aquí tienes tu encuesta aleatoria:")
for pregunta, respuesta in encuesta:
    print(f"* {pregunta}: {respuesta}")
