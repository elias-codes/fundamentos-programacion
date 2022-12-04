#Este programa calcula el bono de un trabajado
GBONO70 = 500
GBONO55 = 250
CBONO70 = 800
CBONO55 = 300
#Escribimos el mensaje de bienvenida y pedimos los datos
print("-Empresas empresariales SA de CV-")
print("Bienvenido este programa calcula el bono del trabajador")
nombre = input("Introduzca su nombre: ")
horas = int(input("Introduzca las horas trabajadas: "))
#Pedimos puesto
print("Seleccione su puesto: ")
print("C: Confianza   G: Gerencial")
puesto = input()

#Checamos si es gerencial o de confianza

if puesto == 'G':
    #Es gerencial checamos la cantidad de hora e imprimimos
    if horas >= 70:
        print("El bono de",nombre,"es de",GBONO70)
    elif horas >= 55:
        print("El bono de",nombre,"es de",GBONO55)
    else:
        print("No obtuvo un bono, buen dia")
elif puesto == 'C':
     #Es gerencial checamos la cantidad de hora e imprimimos
    if horas >= 70:
        print("El bono de",nombre,"es de",CBONO70)
    elif horas >= 55:
        print("El bono de",nombre,"es de",CBONO55)
    else:
        print("Obtuvo un ticket para pizzas")   
else:
    # En caso de que no seleccione C o G
    print("Error puesto no reconocido")
    
        






