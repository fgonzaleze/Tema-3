from threading import Condition, Thread
import time
import random

recolectado = 0 #Bote recaudado
cond = Condition()

class Voluntarios(Thread):

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        global recolectado
        global cond

        print("El voluntario", self.name, "sale a la calle")

        while True:
            colecta = random.randint(4, 25) #El volutario recolecta entre 4 y 25 euros
            print("El voluntario", self.name, "quiere recolectar", colecta, "€")
            cond.acquire()
            while recolectado + colecta > 2000: #Si la suma de lo que quiere recolectar y el bote existente es mayor a 2000, espera
                print("El voluntario", self.name, "tiene que esperar antes de poder ingresar el dinero especificado")
                cond.wait()
            cond.release()

            cond.acquire()
            print("El voluntario", self.name, "está recaudando los", colecta, "€")
            time.sleep(random.randint(1, 3)) #Tiempo que tarda el voluntario en recolectar el dinero

            recolectado += colecta #Una vez recaudado, lo suma al bote conjunto
            cond.notifyAll() #Se notifica el cambio en el bote
            print("El voluntario", self.name, "ha recolectado", colecta, "€. Hay", recolectado, "€ en total.")
            cond.release() 


class Gestores(Thread):
    
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        global recolectado
        global cond

        print("El gestor", self.name, "sale a la calle")

        while True:
            cantidad = random.randint(10, 40) #El gestor recolecta entre 10 y 40 euros
            print("El gestor", self.name, "quiere recolectar", cantidad, "€")

            cond.acquire()
            while recolectado < cantidad: #Si el dinero del bote es menor a la cantidad que desea recaudar el recolector, se espera
                print("El gestor", self.name, "no puede coger los", cantidad, "€ porque solo quedan", recolectado, "€") 
                cond.wait()
            cond.release()

            cond.acquire()

            print("El gestor", self.name, "está recogiendo los", cantidad, "€")
            time.sleep(random.randint(2, 5)) #Tiempo que toma el recolector en recaudar el dinero

            recolectado -= cantidad #Restamos al bote la cantidad recolectada por el gestor y notificamos el cambio al resto de hilos
            cond.notifyAll()
            print("El gestor", self.name, "ha recogido", cantidad, "€. Quedan", recolectado, "€")
            cond.release()
