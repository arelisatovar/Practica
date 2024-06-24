import os
import csv

os.system('cls')

with open('Archivo_Alumnos.csv', 'w', newline='') as archivo:
    voy_a_escribir = csv.writer(archivo)
    voy_a_escribir.writerow(['Nombre','Asignatura','Nota'])

# Validaciones: No se aceptan nombres vacios ni notas fuera de rango ni 

pregunta = 's'
# Crea un programa que tome los datos de un alumno validando que no sea nombre vacio
while pregunta == 's':
    alumno = ''
    while alumno == '':
        alumno = input('Ingrese nombre del alumno: ').strip()

        if alumno == '':
            print('Nombre invalido')
        else:
    # Preguntar cuantas materias esta cursando y en base a eso le pregunte los nombres de las materias
    # No se aceptan numeros de materia = 0 ni fuera de rango
            
            while True:
                try:
                    asignaturas = int(input('Cuantas asignaturas estas cursando? '))
                except:
                    asignaturas = 0
                if asignaturas <1 or asignaturas >7:
                    print('Número de asignaturas no valido, favor ingrresar solo números')
                else:
                    lista_asignaturas = []
                    for asignatura in range(asignaturas):
                        nombres_asignatura = ''
                        while nombres_asignatura == '':
                            nombres_asignatura = input(f'Ingresa el nombre de la asignatura {asignatura+1}: ').strip()
                            if nombres_asignatura == '':
                                print('Favor ingresar un nombre valido')
                            else:
                                lista_asignaturas.append(nombres_asignatura)
# preguntar las notas y finalemnte guardar en un archivo CSV con las cabeceras de: Nombre,Materia,Nota
# No se aceptan notas fuera de rango

                    lista_notas = []
                    for n in lista_asignaturas:
                        while True:
                            try: 
                                notas = float(input(f'Ingrese nota para {n}: '))
                            except:
                                notas = 0
                            if notas < 1 or notas > 7:
                                print('Rango de nota no valido, favor ingrear numero del 1 al 7')
                            else:
                                lista_notas.append(notas)
                                break
                    with open('Archivo_Alumnos.csv', 'a', newline='') as archivo_csv:
                        escribir_datos = csv.writer(archivo_csv)
                        for i in range(len(lista_asignaturas)):
                            escribir_datos.writerow([alumno,f'{lista_asignaturas[i]}',f'{lista_notas[i]}'])
                    break
# El programa debe repetirse N veces 
    pregunta = input('Desea agregar otro alumno? s/n ')
print('Ha salido del programa')

#Extra

# luego consultar el archivo y calcular el promedio de notas de cada alumno
# exportar las notas aprobadas a un Json y las desaprobadas a otro Json