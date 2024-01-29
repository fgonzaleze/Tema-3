# Hay cuatro estudiantes que comparten nueve libros. Los estudiantes seleccionan dos libros al azar y, una vez obtenidos, 
# los utilizan durante un tiempo aleatorio de entre 3  y 5 segundos. En caso de que alguno de los dos libros no estuviese libre, 
# entonces el estudiante se queda esperando hasta que algún libro se libere.
# Una vez han terminado de utilizar los dos libros que han reservado, los devuelven a la vez, de forma que otros estudiantes puedan utilizarlos. 
# Todos los estudiantes han tenido que ser capaces de utilizar sus dos libros.
# Muestra mensajes cada vez que un estudiante coge dos libros y también una vez los libera, donde se indiquen el nombre del estudiante y los libros que ha reservado.


import random
from threading import Thread, Semaphore
import time


class estudiar(Thread):
    semaforo = Semaphore(2)

    def __init__(self,nombre):
        Thread.__init__(self, name = nombre)
    
    def run(self):
        print("El alumno", self.name, "está esperando")
        estudiar.semaforo.acquire()
        print("El alumno", self.name, "está estudiando")
        time.sleep(random.randint(1,10))
        print("El cliente", self.name, "ha terminado de estudiar")
        estudiar.semaforo.release()
