
from threading import Thread
from ejercicio2 import EscapeRoom, Persona

# Hilos de los qe juegan
personas = []
for i in range(5):
    nombre_persona = f"Persona {i+1}"
    hilo_persona = Persona(nombre_persona)
    personas.append(hilo_persona)

# arrancamos los hilos
for persona in personas:
    persona.start()