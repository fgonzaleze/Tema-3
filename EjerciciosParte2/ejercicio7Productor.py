
from multiprocessing import Queue
import random
from threading import Thread, Condition
import time
from main7 import cola, cond

class Productor(Thread):
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        while True:
            cadena = "objeto"
            with cond:
                while not cola.empty():
                    print("La cola está llena")
                    cond.wait()
                cola.put(cadena)  # Llenamos la cola
                print("Hilo", self.name, "produciendo")
                time.sleep(random.randint(1, 5))
                print("Hilo", self.name, "ha terminado de producir")
                cond.notifyAll()
                    
        