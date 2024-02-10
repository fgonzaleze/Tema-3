# Simula una carrera. Al inicio de una carrera todos los participantes parten de la misma línea de salida. 
# Una vez están todos colocados, se comienza una cuenta atrás desde 3. Una vez se dé el pistoletazo de salida entonces saldrán todos. 
# Impleméntalo con 10 hilos e intenta calcular cuánto tiempo tarda cada uno en terminar la carrera.

import threading
import time
import random

class Corredor(threading.Thread):
    def __init__(self, nombre, salida):
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.salida = salida

    def run(self):
        print(f"{self.nombre} está en la línea de salida")
        # Esperamos a que esten listos
        self.salida.wait()
        print("Sale el corredor", self.nombre)
        inicio = time.time()

        # La carrera es un tiempito aleatorio
        time.sleep(random.uniform(3, 10))
        self.tiempo = time.time() - inicio
        print(f"{self.nombre} ha terminado la carrera en {self.tiempo:.2f} segundos.")