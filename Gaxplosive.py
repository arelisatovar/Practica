import os
import json
from funciones import registro_de_pedido
os.system ("cls")

# LISTAS

pedidos = []

# MENU

while True:
    
    print("Bienvenido al menu de GAXPLOSIVE, deberas escoger alguna opcion para continuar")

    print("1.- Registrar pedido: ")
    print("2.- Lista de todos los pedidos: ")
    print("3.- Imprimir hoja de ruta: ")
    print("4.- Salir del programa: ")
    
    try:
        opcion = int(input("ingrese una opcion: \n"))
    
    except:
        opcion = 0
    if opcion <1 or opcion >4:
        print("Opcion no valida, ingrese una opcion: \n")
        
    elif opcion == 1:
        pedido= registro_de_pedido()
        pedidos.append(pedido)
            
    elif opcion == 2:
        print("Lista de todos los pedidos : ")
        if len(pedidos) == 0:
            print("Aqui no hay nada, vuelve a intentarlo")
        
        for pedido in pedidos:
            print(f'{pedido["Nombre"]}\n{pedido["Direccion:"]}\n{pedido["Cilindro de 5 kg:"]}\n{pedido["Cilindro de 15 kg:"]}\n{pedido["Cilindro de 45 kg:"]}')
        
    
    
    elif opcion == 3:
        print("Imprimir hoja de ruta: ")
    else:
        break
