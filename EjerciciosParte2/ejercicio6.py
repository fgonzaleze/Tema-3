
import random
from threading import Condition, Thread
import time


class Filosofo(Thread):
    cond = Condition()
    palillos = [False, False, False, False, False]

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
    
    def run(self):
        while True:
            print("Filosofo", self.name, "está pensando")
            time.sleep(random.randint(1,3))
            print("Filosofo", self.name, "ha pensado")

            with Filosofo.cond:
                while Filosofo.palillos[int(self.name)]:
                    Filosofo.cond.wait()

                Filosofo.palillos[(int(self.name))] = True

                while Filosofo.palillos[(int(self.name)+1)%5]:
                    Filosofo.cond.wait()

                Filosofo.palillos[(int(self.name)+1)%5] = True

            print("Filosofo", self.name, "está comiendo")
            time.sleep(random.randint(1,3))
            print("Filosofo", self.name, "ha terminado de comer")

            with Filosofo.cond:
                Filosofo.palillos[(int(self.name))] = False
                Filosofo.palillos[(int(self.name)+1)%5] = False

                Filosofo.cond.notifyAll()