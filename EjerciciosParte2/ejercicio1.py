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
            NumOculto.lock.acquire()
            if not NumOculto.numAcertado:
                NumOculto.lock.release()
                numAleatorio = random.randint(0,100)
                if numAleatorio == NumOculto.numAdivinar: # Seccion critica
                    NumOculto.lock.acquire()
                    NumOculto.numAcertado = True # Seccion critica
                    NumOculto.lock.release()
                    print("He acertado, soy el hilo", self.name, "el resultado es numAleatorio:", numAleatorio, "numAdivinar", NumOculto.numAdivinar)
                    break
                else:
                    print("El hilo", self.name, "ha generado el numero", numAleatorio, "y ha fallado")
            else:
                NumOculto.lock.release()
                print("Otro hilo ya ha acertado")
                break

