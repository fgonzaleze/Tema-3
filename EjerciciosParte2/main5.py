from ejercicio5 import estudiar

if __name__ == "__main__":
    lista = []
    for i in range(9):
        hilo = estudiar(str(i))
        hilo.start()
        lista.append(hilo)
    
    for h in lista:
        h.join()
    
    print("Todos los alumnos han acabado de estudiar")