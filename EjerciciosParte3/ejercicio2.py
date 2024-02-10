# Simula una sala de Escape Room en la que hay 5 personas encerradas. Para poder salir deben adivinar la clave que abre la puerta que es un código de 4 cifras. 
# Una vez adivinado, deben juntarse los 5 para poder salir juntos y así no dejar a ninguno atrás.



from threading import Lock, Barrier, Thread
import random
import time


class EscapeRoom:
    codigo_secreto = random.randint(0, 20) # He puesto un codigo de 0 a 20 para que vaya mas rapido al adivinar
    codigo_adivinado = False
    lock = Lock()
    barrier = Barrier(5)  # 5 personas (hilos) que esperann en la barrera

class Persona(Thread):
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
    
    def run(self):
        while True:
            with EscapeRoom.lock:
                if not EscapeRoom.codigo_adivinado:
                    num_aleatorio = random.randint(0, 20) 
                    print(f"{self.name} intenta adivinar el código.")
                    #time.sleep(random.randint(1, 2))
                    print(f"{self.name} cree que el código es: {num_aleatorio}.")
                    if num_aleatorio == EscapeRoom.codigo_secreto:
                        EscapeRoom.codigo_adivinado = True
                        print(f"{self.name} ha adivinado el código secreto: {num_aleatorio}!")
                        break
                    else:
                        print(f"{self.name} ha probado el número {num_aleatorio} y no era correcto")
                else:
                    print("Otra persona ya ha acertado.")
                    break
        EscapeRoom.barrier.wait()  # Espera que todos los hilos lleguen a la barrera
        print("Todos han salido")
