from ejercicio4 import carniceria, charcuteria

if __name__ == "__main__":
    lista = []
    for i in range(10):
        hiloCarniceria = carniceria(str(i))
        hiloCarniceria.start()
        lista.append(hiloCarniceria)
        hiloCharcuteria = charcuteria(str(i))
        hiloCharcuteria.start()
        lista.append(hiloCharcuteria)
    
    for h in lista:
        h.join()
    
    print("Todos los clientes han sido atendidos")