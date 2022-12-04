#Este programa nos indica si podemos hacer una declaracion de impuestos
#Declarar constantes
TIJUANA = 100000
ENSENADA = 80000
MEXICALI = 90000
TECATE = 70000
SANQ = 50000
#Imprimimos el mensaje de bienvenida
print("Bienvenido a SUPERSAT")
#Abrimos un while para repetir el programa
while (True):
    #pedimos los datos
    nombre = input("Introduzca su nombre: ")
    edad = int(input("Edad: "))
    sexo = input("Genero: ")
    ingreso = int(input("Ingreso mensual: "))
    municipio = input("""Seleccione su municipio:
    Tijuana = T
    Ensenada = E
    Mexicali = M
    Tecate = T
    San Quintin = S 
    """)
    #Revisamos la edad del usuario
    if edad >= 18:
        #Checamos el municipio del usuario
        if municipio == "T":
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
    else:
        #No es mayor de edad
        print("Es necesario ser mayord de edad para declarar")    
        

