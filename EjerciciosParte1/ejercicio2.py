# Contador compartido
# Crea un programa que utilice 10 hilos para incrementar un contador compartido. Deben dejar de contar cuando el contador llegue a 1000. 
# Para ello, en el método run() se seguirá incrementando la variable mientras ésta sea menor que 1000.
# Para hacer que una variable sea compartida por todos los objetos de una clase declárala a nivel de clase, fuera del constructor:

# Observa cómo la concurrencia puede afectar el resultado final.

from threading import Thread

class Contador(Thread):
    contador = 0

    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)
    
    def run(self):
        # Contador.contador es una variable estática comun entre los objetos
        while Contador.contador < 1000:
            Contador.contador = Contador.contador + 1
            print(Contador.contador)