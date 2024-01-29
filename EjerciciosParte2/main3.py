from ejercicio3 import carniceria

if __name__ == "__main__":
    lista = []
    for i in range(20):
        hilo = carniceria(str(i))
        hilo.start()
        lista.append(hilo)
    
    for h in lista:
        h.join()
    
    print("Todos los clientes han sido atendidos")