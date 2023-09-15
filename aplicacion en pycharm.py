import random

preguntas = ["¿Cuál es tu color favorito?", "¿Cuál es tu animal favorito?", "¿Cuál es tu libro favorito?"]

respuestas = ["Rojo", "Perro", "Harry Potter"]

encuesta = []
for i in range(len(preguntas)):
    encuesta.append((preguntas[i], respuestas[random.randint(0, len(respuestas) - 1)]))

print("Aquí tienes tu encuesta aleatoria:")
for pregunta, respuesta in encuesta:
    print(f"* {pregunta}: {respuesta}")
