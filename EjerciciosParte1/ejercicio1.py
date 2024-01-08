# Hilos trabajadores
# Crea una aplicación en Java que construya 5 hilos a partir de una única clase.
# Cada hilo tiene su propio nombre. Puedes usar nombres de personas para así distinguirlos mejor.
# En el método run debe haber un bucle infinito. Dentro del bucle se hará lo siguiente:
#   Escribe el texto: "Soy nombre y estoy trabajando".
#   Detiene la ejecución durante un período de tiempo aleatorio entre 1 y 10 segundos.
#   Escribe el texto: "Soy nombre y he terminado de trabajar".
# Comprueba que todos los hilos llegan a ejecutarse al menos una vez.

import random
from threading import Thread
import time

class Trabajador(Thread):
    def __init__(self, nombre):
        Thread.__init__(self)
        self.nombre = nombre

    def run(self):
        while True:
            print("Soy", self.nombre, "y estoy trabajando")
            tiempoTrabajo = random.randint(1,10)
            time.sleep(tiempoTrabajo) #Simula el tiempo de trabajo
            print("Soy", self.nombre, "y he terminado de trabajar. He trabajado:", tiempoTrabajo, "horas")