# A la carnicería del ejercicio anterior le ha ido bien y ha ampliado el local, añadiendo también una sección de Charcutería. 
# Como el sistema de hilos que implementaste le gustó, te ha pedido que lo vuelvas a implementar pero añadiendo la Charcutería. Ten en cuenta lo siguiente para realizarlo:
#   - En la Carnicería sigue habiendo 4 personas trabajando, pero en la Charcutería solo 2.
#   - Todos los clientes van a pasar tanto por la Charcutería como por la Carnicería.
#   - Si la Carnicería está llena (es decir, ya están las 4 personas ocupadas) pero en la Charcutería hay algún trabajador libre, 
#   el cliente que esté esperando para ser atendido por Charcutería será atendido. Y viceversa, si en la Charcutería están todos ocupados pero en la Carnicería hay alguien libre, 
#   y algún cliente está pendiente de ser atendido por Carnicería, puede ser atendido por ella.
#   - Un cliente está completamente servido cuando ha sido atendido tanto por Carnicería como por Charcutería, y no siempre tiene que ser en este orden.
# El método main debe lanzar 10 hilos. Establece un nombre para cada hilo. Escribe mensajes tanto para cuando el cliente esté siendo atendido en 
# Carnicería como si está siendo atendido en Charcutería. Establece un tiempo aleatorio de atención al cliente tanto en la charcutería como en la carnicería.

import random
from threading import Semaphore, Thread
import time

class carniceria(Thread):
    semaforo = Semaphore(4)

    def __init__(self,nombre):
        Thread.__init__(self, name = nombre)
    
    def run(self):
        print("El cliente", self.name, "está esperando en la carnicería")
        carniceria.semaforo.acquire()
        print("El cliente", self.name, "está siendo atendido en la carnicería")
        time.sleep(random.randint(1,10))
        print("El cliente", self.name, "ha terminado en la carnicería")
        carniceria.semaforo.release()

class charcuteria(Thread):
    semaforo = Semaphore(2)

    def __init__(self,nombre):
        Thread.__init__(self, name = nombre)
    
    def run(self):
        print("El cliente", self.name, "está esperando en la charcutería")
        carniceria.semaforo.acquire()
        print("El cliente", self.name, "está siendo atendido en la charcutería")
        time.sleep(random.randint(1,10))
        print("El cliente", self.name, "ha terminado en la charcutería")
        carniceria.semaforo.release()