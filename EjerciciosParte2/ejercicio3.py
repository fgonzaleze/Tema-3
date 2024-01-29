# Programa un sistema multihilo que gestione la cola de una carnicería. La carnicería tiene 4 empleados, por lo que puede haber 4 clientes pidiendo a la vez. 
# Una vez estén ocupados los 4 el resto de clientes deben esperar.
# El método main deberá lanzar 10 hilos. Establece un nombre para cada hilo. Una vez que ese hilo esté siendo atendido en la carnicería, debe mostrar el mensaje:
# "El cliente x está siendo atendido".
# Tras una espera aleatoria de entre 1 y 10 segundos (porque el carnicero tarda un tiempo en preparar la carne), se debe mostrar el mensaje:
# "El cliente x ha terminado en la carnicería".

import random
from threading import Semaphore, Thread
import time

class carniceria(Thread):
    semaforo = Semaphore(4)

    def __init__(self,nombre):
        Thread.__init__(self, name = nombre)
    
    def run(self):
        print("El cliente", self.name, "está esperando")
        carniceria.semaforo.acquire()
        print("El cliente", self.name, "está siendo atendido")
        time.sleep(random.randint(1,10))
        print("El cliente", self.name, "ha terminado en la carnicería")
        carniceria.semaforo.release()
