# Este programa indica la cantidad a pagar a un 
# trabajador de contruccion por dia
VALOR_BLOQUE = 4
VALOR_DESPERDICIO = 6

#Mensaje de bienvenida

print("Bienvenido a ConstruPay")
print("Este programa calcula la cantidad a pagar al trabajador")

#Se le piden los datos al operador

bloques = int(input("Favor de introducir la cantidad de bloques colocados: "))
desperdicio = int(input("Introduzca la cantidad de bloques desperdiciados: "))
gastos = int(input("Cuando gasto en la tienda?: "))

#Calculamos el pago del dia

pago = bloques * VALOR_BLOQUE - desperdicio * VALOR_DESPERDICIO - gastos

#Muestra el resultado

print("El pago del dia sera de: $"+str(pago))
