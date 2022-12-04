#Escribimos un mensaje de bienvenida
print("Este programa recibe solo numeros positivos")
#inicializamos variable en 1
#Pedimos los numeros
numero = int(input("Introduzca un numero positivo: "))
#este while corre hasta que introduzca un numero positivo
while numero < 0:
    #pedimos de nuevo el numero si es negativo
    numero = int(input("Error, numero negativo, introduzca de nuevo: "))

print("Numero positivo, gracias")