# Vuelve a realizar este ejercicio de la PARTE 1 pero utilizando Lock() como método de sincronización para asegurarte de que una vez que se averigüe el número, 
# el resto de hilos no generan de nuevo el número.

import threading
import random

class NumOculto(threading.Thread):
    numAdivinar = random.randint(0,100)
    numAcertado = False
    lock = threading.Lock()

    def __init__(self, nombre):
        threading.Thread.__init__(self, name = nombre)
    
    def run(self):
        
        while True:
            numAleatorio = random.randint(0,100)
            NumOculto.lock.acquire()
            if numAleatorio == NumOculto.numAdivinar:
                
                print("He acertado, soy el hilo", self.name, "el resultado es numAleatorio:", numAleatorio, "numAdivinar", NumOculto.numAdivinar)
                NumOculto.numAcertado = True
                
            
            elif NumOculto.numAcertado == True:
                print("Ya se ha acertado el numero")
                break
            # NumOculto.lock.notifyAll()
            NumOculto.lock.release()

