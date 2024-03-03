from ejercicio1 import Cliente

if __name__ == "__main__":
    clientes = []
    for i in range(1, 11):
        cliente = Cliente(str(i))
        clientes.append(cliente)
        cliente.start()

    for cliente in clientes:
        cliente.join()

    print("Todos los clientes han sido atendidos")