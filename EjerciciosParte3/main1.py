
import random
from threading import Event
import time

from ejercicio1 import Corredor


if __name__ == "__main__":
    # Evento para el inicio de carrera
    salida = Event()

    # Creamos los corredores
    corredores = []
    for i in range(10):
        nombre = f"número {i+1}"
        corredor = Corredor(nombre, salida)
        corredores.append(corredor)

    # Esperams a que esten colocadps
    print("Los corredores se estan preparando")
    time.sleep(random.randint(1, 5))

    # Se estan preparando
    print("Los corredores se preparan en la linea de salida")
    for corredor in corredores:
        corredor.start()

    # Cuenta atras para el tiro 
    print("Cuenta atrás!")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    # Para cuando salen
    print("BANG") # pistoletazo de salida
    salida.set()


