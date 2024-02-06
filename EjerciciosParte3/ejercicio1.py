# Simula una carrera. Al inicio de una carrera todos los participantes parten de la misma línea de salida. 
# Una vez están todos colocados, se comienza una cuenta atrás desde 3. Una vez se dé el pistoletazo de salida entonces saldrán todos. 
# Impleméntalo con 10 hilos e intenta calcular cuánto tiempo tarda cada uno en terminar la carrera.

import random
from threading import Thread, Timer
import time


class Carrera(Thread):

    
    def __init__(self, nombre):
        Thread.__init__(self)
        self.nombre = nombre

    def run(self):
        temporizador = Timer(3, function)
        print("El cliente", self.name, "está esperando en la carnicería")
        Carrera.semaforo.acquire()
        print("El cliente", self.name, "está siendo atendido en la carnicería")
        time.sleep(random.randint(1,10))
        print("El cliente", self.name, "ha terminado en la carnicería")
        