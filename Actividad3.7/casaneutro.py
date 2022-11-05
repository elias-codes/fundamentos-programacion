TDC = 19.50
COMISION = 70

# Aqui se muestra el mensaje de bienvenida y captura los datos
print("Bienvenido a Casa de Cambio")
print("Este servicio tiene una comision en pesos de", COMISION)
nombre = input("Cual es su nombre:? ")
trabajo = input("Cual es su trabajo? ")

# Solicita la cantidad de dolares a cambiar
dolares = int(input("De cuantos dolares es su cheque? "))

# Convierte la cantidad a pesos menos la comision
pesos = (dolares * TDC) - 70

# Muestra el resultado
print("Bienvenido", nombre)
print("Su cheque en pesos es de:", pesos)
