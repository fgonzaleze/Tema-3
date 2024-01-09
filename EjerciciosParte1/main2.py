
from ejercicio2 import Contador

if __name__ == "__main__":
     for i in range(0,10):
         hilo = Contador(f"hilo{i}")
         hilo.start()
