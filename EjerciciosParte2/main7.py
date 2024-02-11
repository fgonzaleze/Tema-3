from queue import Queue
from threading import Condition
from ejercicio7Consumidor import Consumidor
from ejercicio7Productor import Productor


if __name__ == "__main__":
    cola = Queue(1)
    cond = Condition()

    prod = Productor("prod")
    cons = Consumidor("cons")

    cons.start()
    prod.start()