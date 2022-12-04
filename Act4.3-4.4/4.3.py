#Se muestra el nombre del programa
print("Buscando Multiplos")
#Se inicializan las variables
cuenta = 0
cont22 = 0
#Pedimos el rango de numeros
inicial = int(input("Ingresa rango inicial: "))
final= int(input("Ingresa rango final: "))
#pedimos el multiplo a buscar
multiplo = int(input("Multiplo a buscar: "))

 
#Revisamos el residuo de cada uno de los numeros
for i in range(inicial,final):

  if i % 2 == 0:
    print(i) #imprimimos los multiplos
    cuenta = cuenta + 1
#restamos la cantidad de multiplos a los numeros revisados, para sacar el numero de no multiplos
cont22 = final - inicial - cuenta
   
#Imprimimos los multiplos encontrados
print(f"Desde {inicial} hasta {final - 1} hay {cuenta} múltiplos de {multiplo}")
#Imprimimos los no multiplos encontrados
print(f"Desde {inicial} hasta {final - 1} hay {cont22} que NO son múltiplos de {multiplo}")