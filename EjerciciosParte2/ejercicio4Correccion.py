import random
from threading import Semaphore, Thread
import time


class Carniceria2(Thread):
    carniceria = Semaphore(4)
    charcuteria = Semaphore(2)

    def __init__(self,nombre):
            Thread.__init__(self, name = nombre)

    def run(self):
        carniceria = False
        charcuteria = False
        print("Llega el cliente", self.name)
        while not carniceria or not charcuteria:
                if Carniceria2.carniceria._value > 0 and not carniceria: # Para saber que aun quedan
                    with Carniceria2.carniceria: # Bloquea el segmento del codigo
                        carniceria = True
                        print("El cliente", self.name, "está siendo atendido en carniceria")
                        time.sleep(random.randint(1,5))
                        print("El cliente", self.name, "ha terminado en la carniceria")
                if Carniceria2.charcuteria._value > 0 and not charcuteria:
                     with Carniceria2.charcuteria: # Bloquea el segmento de código
                        charcuteria = True
                        print("El cliente", self.name, "está siendo atendido en charcuteria")
                        time.sleep(random.randint(1,5))
                        print("El cliente", self.name, "ha terminado en la charcuteria")
        print("El cliente", self.name, "ha terminado de comprar")
            
