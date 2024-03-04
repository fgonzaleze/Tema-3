import random
from threading import Condition, Thread
import time

class Persona(Thread):
    cond = Condition()
    coloresPrimarios = ["amarillo", "magenta", "cian"]
    coloresSecundarios = ["rojo", "azul", "verde"]
    cubosPintura = {}
    for color in coloresPrimarios:
        cubosPintura[color] = False

    def __init__(self, nombre, colorSecundario):
        Thread.__init__(self, name=nombre)
        self.colorSecundario = colorSecundario

    def run(self):
        while True:
            color1, color2 = self.obetenerColoresPrimarios()
            self.prepararColor(color1, color2)
            print(f"{self.name} pinta del color {self.colorSecundario}")
            time.sleep(random.uniform(1, 2))

    def obetenerColoresPrimarios(self):
        if self.colorSecundario == "rojo":
            return "amarillo", "magenta"
        elif self.colorSecundario == "azul":
            return "magenta", "cian"
        elif self.colorSecundario == "verde":
            return "amarillo", "cian"

    def prepararColor(self, color1, color2):
        with Persona.cond:
            while Persona.cubosPintura[color1] or Persona.cubosPintura[color2]:
                print(f"{self.name} espra los cubos de pintura para hacer {self.colorSecundario}")
                Persona.cond.wait()

            Persona.cubosPintura[color1] = True
            Persona.cubosPintura[color2] = True
            print(f"{self.name} ha cogido los cubos de pintura para hacer {self.colorSecundario}")
            time.sleep(random.uniform(0.1, 0.5))
            print(f"{self.name} ha preparado {self.colorSecundario}")

            Persona.cubosPintura[color1] = False
            Persona.cubosPintura[color2] = False

            Persona.cond.notify_all()



