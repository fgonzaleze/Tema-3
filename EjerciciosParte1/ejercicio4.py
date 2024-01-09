# Repite el ejercicio de contar vocales que se hizo en el tema de multiprocesos pero utilizando hilos. 
# Habrá que lanzar 5 hilos y cada hilo contará una vocal distinta.

# Crea un proceso que cuente las vocales de un fichero de texto. Para ello crea una función que reciba una vocal y 
# devuelva cuántas veces aparece en un fichero. Lanza el proceso de forma paralela para las 5 vocales. 
# Tras lanzarse se imprimirá el resultado por pantalla.

from threading import Thread

fichero = "EjerciciosParte1/vocales.txt"

class ContarVocales(Thread):

    def __init__(self, letra):
        Thread.__init__(self, name=letra)
        self.letra = letra

    def run(self):
        contador = 0
        with open(fichero, "r") as archivo:
            letras = archivo.read()
            contador = letras.count(self.letra)
        if contador == 1:
            print("La letra", self.letra, "aparece", contador, "vez")
        else: 
            print("La letra", self.letra, "aparece", contador, "veces")

