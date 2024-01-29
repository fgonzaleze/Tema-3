from ejercicio4Correccion import Carniceria2

if __name__ == "__main__":
    for i in range(0,10):
        hilo = Carniceria2(f"{i}")
        hilo.start()
    print("Todos han terminado de comprar")
    


