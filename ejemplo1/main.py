from ejemplo1.hilos1 import hilos1


print("Soy el hilo principal")

for i in range (0,10):
    hilo = hilos1(i)
    hilo.start()

hilo.join()

