
import random
from threading import Thread
import time
from main7 import cond, cola


class Consumidor(Thread):
    def __init__(self,nombre):
        Thread.__init__(self, name = nombre)

    def run(self):
        while True:
            with cond:
                while cola.full():
                    print("Cola vacía")
                    cond.wait()
                cadena = cola.get()
            print(self.name, "está cogiendo el objeto")
            time.sleep(random.randint(1,5))
            print("Objeto recogido",self.name, ":", cadena)
            cond.notifyAll() # Avisa a los productores 