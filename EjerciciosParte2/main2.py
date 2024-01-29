from ejercicio2 import panaderia

if __name__ == "__main__":
    listaClientes = []
    for i in range(20):
        hilo = panaderia(str(i))
        hilo.start()
        listaClientes.append(hilo)
    
    for h in listaClientes:
        h.join()
    
    print("Todos tiene pan")