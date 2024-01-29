import random
from threading import Condition, Thread
import time

class Libro(Thread):
    libreria = []
    cond = Condition()
    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)

    def run(self):
        seleccionados = random.sample(range(9), 2) # Devuelve una lista con los dos numeros sin repetir 
        libro1 = seleccionados[0]
        libro2 = seleccionados[1]
        Libro.cond.acquire()
        while Libro.libreria[libro1] or Libro.libreria[libro2]:
            print("El estudiante", self.name, "está esperando los libros", libro1, libro2)
            Libro.cond.wait()

        # Me quedo los libros poniendolos a true
        Libro.libreria[libro1] = True
        Libro.libreria[libro2] = True
        Libro.cond.release()

        print("El estudiante", self.name, "está leyendo los libros", libro1, libro2)
        time.sleep(random.randint(3,5))
        print("El estudiante", self.name, "ha terminado de leer los libros", libro1, libro2)

        # Bloqueo porque modifico la lista, siempre que se modifique se bloquea
        Libro.cond.acquire()
        Libro.libreria[libro1] = False
        Libro.libreria[libro2] = False
        Libro.cond.notifyAll()
        Libro.cond.release()
        print("El estudiante", self.name, "termina de leer los libros", libro1, libro2)
