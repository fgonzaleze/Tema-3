# Vuelve a realizar este ejercicio de la PARTE 1 pero utilizando Lock() como método de sincronización para asegurarte de que una vez que se averigüe el número, 
# el resto de hilos no generan de nuevo el número.

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