# A continuación, se presenta una variante del típico problema de PRODUCTORES y CONSUMIDORES. En este tipo de problemas, 
# uno o más procesos PRODUCTORES ponen datos a disposición de uno o más procesos CONSUMIDORES.
# Si un proceso CONSUMIDOR intenta obtener un dato y no hay ninguno disponible, debe esperar a que algún proceso productor introduzca alguno.
# Los datos se suelen poner en una cola (queue.Queue), de la que se extraen los elementos en el mismo orden en que se introducen, 
# según un planteamiento FIFO o first in, first out. 
# Se puede limitar el número de elementos que se admiten en la cola, de manera que, cuando contiene el máximo número de datos, 
# antes de introducir uno nuevo, los PRODUCTORES deben esperar a que algún proceso CONSUMIDOR retire uno.
# Realiza este ejercicio para el caso en el que la COLA sólo pueda almacenar un dato.
# ¿Cambiaría mucho la solución si el máximo a almacenar son 5 elementos?


from multiprocessing import Queue
import random
from threading import Condition, Thread
import time

cola = Queue(5)  # La capacidad de la cola
cond = Condition()  # Condition para sincronizar lo hilos

class Productor(Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def run(self):
        while True:
            with cond:
                while not cola.empty():
                    print("La cola está llena. El productor", self.nombre, "espera.")
                    cond.wait()
                item = "Coso"
                cola.put(item)  # Ponemos el dato en la cola
                print("Productor", self.nombre, "produce el elemento", item)
                time.sleep(random.randint(1, 3))
                cond.notify_all()  # Notificamos a los consumidores

class Consumidor(Thread):
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        while True:
            with cond:
                while cola.empty():
                    print("La cola está vacía. El consumidor", self.name, "espera.")
                    cond.wait()
                item = cola.get()  # Obtenemos un elemento de la cola
                print("Consumidor", self.name, "consume el elemento", item)
                time.sleep(random.randint(1, 3))
                cond.notify_all()  # Notificamos a los productores

# Creamos productores y consumidores
productores = [Productor(f"{i}") for i in range(3)]
consumidores = [Consumidor(f"{i}") for i in range(2)]

if __name__ == "__main__":
    # Iniciamos los productores y consumidores
    for p in productores:
        p.start()

    for c in consumidores:
        c.start()
