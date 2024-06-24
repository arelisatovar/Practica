import os
os.system ("cls")

while True:
    
    print("Bienvenido al menu de GAXPLOSIVE, deberas escoger alguna opcion para continuar")

    print("1.- Registrar pedido: ")
    print("2.- Lista de todos los pedidos: ")
    print("3.- Imprimir hoja de ruta: ")
    print("4.- Salir del programa: ")
    
    try:
        opcion=int(input("Ingrese una opcion del menu: \n"))
    except:
        opcion= -1
    if opcion >0 or opcion < 4:
        print("Ingresa una opcion valida")
    
    if opcion == 1:
        print("registre al usuario:\n")
        
        validacion_c = ""
        while validacion_c == "":
            c= input ("ingresa nombre del cliente: \n")
            validacion_c = c.replace (" ","")
            if validacion_c == "":
                print("Nombre invalido")