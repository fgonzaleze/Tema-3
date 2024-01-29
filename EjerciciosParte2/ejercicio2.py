# Simula el comportamiento de la cola de una panadería en la que sólo hay un dependiente, por lo que los clientes son atendidos de uno en uno. 
# Imprime mensajes donde se vea qué hilos están esperando a ser atendidos y cuáles están siendo atendidos. 
# El dependiente tarda un tiempo aleatorio entre 1 y 5 segundos en atender a cada cliente.

import random
from threading import Semaphore, Thread
import time


class panaderia(Thread):
    semaforo = Semaphore()

    def __init__(self,nombre):
        Thread.__init__(self, name = nombre)
    
    def run(self):
        print("El hilo", self.name, "está esperando")
        panaderia.semaforo.acquire()
        print("El hilo", self.name, "está en caja")
        time.sleep(random.randint(1,5))
        print("El hilo", self.name, "ya ha pagado")
        panaderia.semaforo.release()
            