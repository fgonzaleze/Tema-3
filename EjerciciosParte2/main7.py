
from ejercicio7Productor import *
from ejercicio7Consumidor import *
from queue import Queue
from threading import Condition


if __name__ == "__main__":
    cola = Queue(1)
    cond = Condition()

    prod = Productor("prod")
    cons = Consumidor("cons")

    cons.start()
    prod.start()