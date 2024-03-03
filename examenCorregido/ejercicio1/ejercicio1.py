import random
from threading import Semaphore, Thread
import time

class Cliente(Thread):
    semaforo_maquina = Semaphore(2)
    semaforo_dependiente = Semaphore(1)

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        print("El cliente", self.name, "está esperando su turno")
        self.usar_maquina()
        self.obtener_ticket()
        self.obtener_hamburguesa()
        print("El cliente", self.name, "ha sido atendido")

    def usar_maquina(self):
        Cliente.semaforo_maquina.acquire()
        print("El cliente", self.name, "está siendo atendido en la maquina")
        time.sleep(random.randint(1, 4))
        print("El cliente", self.name, "ha obtenido el ticket")
        Cliente.semaforo_maquina.release()

    def obtener_ticket(self):
        pass  # Simplemente se simula con un tiempo de espera

    def obtener_hamburguesa(self):
        Cliente.semaforo_dependiente.acquire()
        print("El cliente", self.name, "está esperando su hamburguesa")
        time.sleep(random.randint(3, 7))
        print("El cliente", self.name, "ha recibido su hamburguesa")
        Cliente.semaforo_dependiente.release()