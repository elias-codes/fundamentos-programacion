BLOQUE = 4
DESPERDICIO = 6

# Aqui se muestra el mensaje de bienvenida y captura los datos
print("Bienvenido a CONSTRUPAGO")
bloques = int(input("Cuantos bloques se colocaron? "))
desperdicios = int(input("Cuanto bloques se desperdiciaron? "))
gastos = int(input("Cuando se gasto en la tiendita?: "))

# Calcula el pago
paga = (bloques * BLOQUE) - (desperdicios * DESPERDICIO) - gastos

# Muestra el resultado
print("El pago del dia sera de:", paga)
