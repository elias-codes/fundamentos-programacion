#Este programa nos indica si podemos hacer una declaracion de impuestos
#Declarar constantes
TIJUANA = 100000 / 12
ENSENADA = 80000 / 12
MEXICALI = 90000 / 12
TECATE = 70000 / 12
SANQ = 50000 / 12

#Imprimimos el mensaje de bienvenida
print("Bienvenido a SUPERSAT")

#Abrimos un while para repetir el programa
while (True):
    #pedimos los datos
    nombre = input("Introduzca su nombre: ")
    edad = int(input("Edad: "))
    sexo = input("Genero: ")
    ingreso = int(input("Ingreso mensual: "))
    municipio = int(input("""Seleccione su municipio:
    1 = Tijuana
    2 = Ensenada
    3 = Mexicali
    4 = Tecate
    5 = San Quintin
    """))

    #Revisamos la edad del usuario
    if edad >= 18:
        #Checamos el municipio del usuario
        if municipio == 1:
            #Comparamos los ingresos
            if ingreso >= TIJUANA:
                #Cumple con los requisitos imprimimos mensaje
                print("Hola",nombre)
                print("Sus datos son: ")
                print("Edad:",edad)
                print("Municipio: Tijuana")
                print("Usted puede declarar")
            else:
                #Si no tiene el ingreso necesario
                print("Usted no cumple con los ingresos minimos")

        elif municipio == 2:
            #Comparamos los ingresos
            if ingreso >= ENSENADA:
                #Cumple con los requisitos imprimimos mensaje
                print("Hola",nombre)
                print("Sus datos son: ")
                print("Edad:",edad)
                print("Municipio: Ensenada")
                print("Usted puede declarar")
            else:
                #Si no tiene el ingreso necesario
                print("Usted no cumple con los ingresos minimos")

        elif municipio == 3:
            #Comparamos los ingresos
            if ingreso >= MEXICALI:
                #Cumple con los requisitos imprimimos mensaje
                print("Hola",nombre)
                print("Sus datos son: ")
                print("Edad:",edad)
                print("Municipio: Mexicali")
                print("Usted puede declarar")
            else:
                #Si no tiene el ingreso necesario
                print("Usted no cumple con los ingresos minimos")

        elif municipio == 4:
            #Comparamos los ingresos
            if ingreso >= TECATE:
                #Cumple con los requisitos imprimimos mensaje
                print("Hola",nombre)
                print("Sus datos son: ")
                print("Edad:",edad)
                print("Municipio: Tecate")
                print("Usted puede declarar")
            else:
                #Si no tiene el ingreso necesario
                print("Usted no cumple con los ingresos minimos")
        
        elif municipio == 5:
            #Comparamos los ingresos
            if ingreso >= SANQ:
                #Cumple con los requisitos imprimimos mensaje
                print("Hola",nombre)
                print("Sus datos son: ")
                print("Edad:",edad)
                print("Municipio: San Quintin")
                print("Usted puede declarar")
            else:
                #Si no tiene el ingreso necesario
                print("Usted no cumple con los ingresos minimos")
    else:
        #No es mayor de edad
        print("Es necesario ser mayor de edad para declarar")  

    #pregunta de salida
    salida = input("Desea continuar en el programa? (si/no): ")  
    if salida == "no":
        break

#mensaje de salida
print("Gracias por utilizar el servicio de SUPERSAT")
    
        

