# Número oculto
# Se debe generar un número al azar entre cero y cien, que deben intentar adivinar otros diez hilos. 
# El número a adivinar se almacenará en una variable de clase. 
# Dentro del método run() se debe implementar la siguiente lógica:
# El hilo genera un número aleatorio.
# Se comprueba si el número generado coincide con el que hay que acertar:
# En caso afirmativo, se termina la ejecución del hilo.
# En caso contrario, hay que comprobar si otro hilo ya ha acertado. Para ello habrá que crear otra variable de clase que lo controle:
# Si otro hilo ya ha acertado, entonces se termina la ejecución del hilo.
# Si todavía nadie ha acertado, se sigue con la búsqueda del número a acertar.

from threading import Thread
import random

class NumOculto(Thread):
    numAdivinar = random.randint(0,100)
    numAcertado = False

    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)
    
    def run(self):
        while True:
            numAleatorio = random.randint(0,100)
            if NumOculto.numAcertado:
                print("Ya se ha acertado el número")
            elif numAleatorio == NumOculto.numAdivinar:
                print("He acertado el numero. Soy", self.name)
                NumOculto.numAcertado = True