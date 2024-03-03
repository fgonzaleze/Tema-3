from ejercicio1 import Hamburguesería

if __name__ == "__main__":
    numeroClientes = 10 #Número de clientes que van a entrar en la Hamburguesería
    clientes = [] 

#Iteramos los clientes
    for i in range(numeroClientes):
        hilo = Hamburguesería(str(i)) #Creamos un cliente en cada iteración
        clientes.append(hilo) 
        hilo.start() #Iniciamos el cliente
    
    for hilo in clientes:
        hilo.join() 

    print("Todos tienen su hamburguesa")