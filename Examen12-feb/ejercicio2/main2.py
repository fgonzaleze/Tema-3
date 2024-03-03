import random
from threading import Condition, Thread
import time

cond = Condition()  # Condition para sincronizar los hilos
count = 0  # Variable global para llevar la cuenta compartida de los ingresos
MAX_AMOUNT = 2000  # Cantidad máxima permitida en la colecta

class Voluntario(Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def run(self):
        global count
        while True:  # Ciclo infinito para que los voluntarios sigan ingresando dinero
            with cond:  # Bloque cond para no llamar explícitamente a acquire y release.
                while count >= MAX_AMOUNT:
                    print("La colecta está llena. El voluntario", self.nombre, "espera.")
                    cond.wait()
                ingreso = random.randint(4, 25)  # El ingreso que hará el voluntario
                count += ingreso
                print("Voluntario", self.nombre, "ingresa", ingreso, "€")
                print("En la colecta hay", count, "€")
                time.sleep(random.randint(1, 3))
                cond.notify_all()  # Notificamos a los gestores

class Gestor(Thread):
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        global count
        while True:  # Ciclo infinito para que los gestores sigan retirando dinero
            with cond:  # Bloque cond para no llamar explícitamente a acquire y release.
                while count < 10:  # Esperar hasta que haya suficiente dinero en la colecta
                    print("La colecta tiene", count, "€. El gestor", self.name, "espera.")
                    cond.wait()
                retirada = random.randint(10, 40)  # La retirada que hará el gestor
                while count < retirada:
                    print("La colecta tiene", count, "€. El gestor", self.name, "espera.")
                    cond.wait()
                count -= retirada  # Retirar dinero de la colecta
                print("Gestor", self.name, "saca:", retirada, "€")
                print("En la colecta hay", count, "€")
                time.sleep(random.randint(2, 5))
                cond.notify_all()  # Notificamos a los voluntarios

# Crear instancias de voluntarios y gestores
voluntarios = [Voluntario(str(i)) for i in range(4)]
gestores = [Gestor(str(i)) for i in range(4)]

if __name__ == "__main__":
    # Iniciar los hilos
    for v in voluntarios:
        v.start()

    for g in gestores:
        g.start()

    # Esperar a que los hilos terminen
    for v in voluntarios:
        v.join()

    for g in gestores:
        g.join()

    print("Todos los voluntarios y gestores han terminado.")

