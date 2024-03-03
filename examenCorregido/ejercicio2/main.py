from ejercicio2 import Voluntarios, Gestores

if __name__ == "__main__":
    cantidadGestores = 4
    cantidadVoluntarios = 4

#Itemo por voluntarios y voy creando un voluntario con cada iteración
    for v in range(cantidadVoluntarios):
        hilo = Voluntarios(str(v))
        hilo.start()

#Hago lo mismo para los gestores
    for g in range(cantidadGestores):
        hilo = Gestores(str(g))
        hilo.start()