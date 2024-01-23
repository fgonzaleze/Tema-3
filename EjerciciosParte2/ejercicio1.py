# Vuelve a realizar este ejercicio de la PARTE 1 pero utilizando Lock() como método de sincronización para asegurarte de que una vez que se averigüe el número, 
# el resto de hilos no generan de nuevo el número.

from threading import Lock, Thread
import random

class NumOculto(Thread):
    numAdivinar = random.randint(0,100)
    numAcertado = False
    lock = Lock()

    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)
    
    def run(self):
        
        while True:
            numAleatorio = random.randint(0,100)
            NumOculto.lock.acquire()
            if numAleatorio == NumOculto.numAdivinar:
                
                print("He acertado, soy el hilo", self.name, "el resultado; numAleatorio:", numAleatorio, "numAdivinar", NumOculto.numAdivinar)
                NumOculto.numAcertado = True
                break
            
            elif NumOculto.numAcertado == True:
                print("Ya se ha acertado el numero")
            NumOculto.lock.release()
            