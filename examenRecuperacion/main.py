from examenRecuperacion import Persona

if __name__ == "__main__":
    personas = []

    personas.append(Persona("Alicia", "rojo"))
    personas.append(Persona("Benito", "azul"))
    personas.append(Persona("Carlos", "verde"))

    for persona in personas:
        persona.start()

    for persona in personas:
        persona.join()