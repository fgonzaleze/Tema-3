from threading import Thread
import time

# Es mejor hacerlo como el otro ejemplo, con herencias

def comer(nombre, tiempoComer):
    print("El raton", nombre, "empieza a comer")
    time.sleep(tiempoComer) #Simula el tiempo de alimentacion del raton
    print("El ratón", nombre, "ha terminado de comer")

if __name__ == "__main__":
    r1 = Thread(target = comer, args=("Mickey", 4))
    r2 = Thread(target = comer, args=("Minnie", 5))
    r3 = Thread(target = comer, args=("Perez", 2))
    
    r1.start()
    r2.start()
    r3.start()