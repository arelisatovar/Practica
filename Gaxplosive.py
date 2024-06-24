import os
import json
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
        print("Registra tu pedido: ")
        val_cliente = ""
        while val_cliente == "":
            cliente = input("Ingresa Nombre y Apellido: \n")
            val_cliente = cliente.replace(" ", "")
            if val_cliente == "":
                print("nombre invalido")
        
        val_direccion = ""
        while val_direccion == "":
            dirrecion = input ("Ingresa la direccion del pedido: \n")
            val_direccion = dirrecion.replace(" ", "")
            if val_direccion == "":
                print ("direccion incorrecta, ingrese la valida")
        
        while True:
            try:
                cil_5kg = int(input("Cilindros de 5KG, limite de 5 cilindros: \n"))
            except:
                cil_5kg= -1          
            if cil_5kg <0 or cil_5kg > 5:
                print("cantidad invalida, ingrese la valida")
            else:
                break
        
        while True:
            try:
                cil_15kg = int(input("Cilindros de 15KG, limite de 5 cilindros: \n"))
            except:
                cil_15kg= -1          
            if cil_15kg <0 or cil_15kg > 5:
                print("cantidad invalida, ingrese la valida")
            else:
                break
        
        while True:
            try:
                cil_45kg = int(input("Cilindros de 45KG, limite de 5 cilindros: \n"))
            except:
                cil_45kg= -1          
            if cil_45kg <0 or cil_45kg > 5:
                print("cantidad invalida, ingrese la valida")
            else:
                break
        
        pedido = { 
                "Nombre:": cliente, 
                "Direccion:": dirrecion, 
                "Cilindro de 5 kg:": cil_5kg, 
                "Cilindro de 15 kg:": cil_15kg, 
                "Cilindro de 45 kg:": cil_45kg
            
        }  
        
        pedidos.append(pedido)
        
    elif opcion == 2:
        print("Registra tu pedido: ")
        if len(pedidos) == 0:
            print("No hay nada, vuelve a intentarlo")
        
        for pedido in pedidos:
            print(f'{pedido["Nombre:"]}\n{pedido["Direccion:"]}\n{pedido["Cilindro de 5 kg:"]}\n{pedido["Cilindro de 15 kg:"]}\n{pedido["Cilindro de 45 kg:"]}\n')
    
    
    elif opcion == 3:
        print("Registra tu pedido: ")
    
    else:
        break
print("hasta luego")
