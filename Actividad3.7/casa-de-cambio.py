# Este programa cambia el cheque de los trabajadores 
# de pesos a dolares y cobra una comision de 70 MXN
tipoDeCambio = 20
COMISION = 70
NOMBRE_CASA = 'Casa de cambio Playas'
nombreCliente = ''
lugarTrabajo = ''
dolares = 0
pesos = 0

# Aqui se muestra el mensaje de bienvenida
# y el nombre de la casa de cambio

print("Bienvenido a ",NOMBRE_CASA)
print("Este programa convierte su cheque en dolares a pesos")
print("Este servicio tiene una comision de $"+str(COMISION)+" pesos")

# Solicitamos el nombre y lugar de trabajo al 

nombreCliente = input("> Favor de introducir su nombre: ")
lugarTrabajo = input("> Favor de introducir su lugar de trabajo: ")

# Aqui solicitamos la cantidad de dolares a cambiar

dolares = int(input("> Introduzca los dolares de su cheque: "))

# Convertimos la cantidad a pesos y restamos la comision

pesos = dolares * tipoDeCambio - 70

# Convierte el formato del resultado a dos decimales

resultado = "{:.2f}".format(pesos)

# Mostramos el resultado de la operacion

print("Bienvenido", nombreCliente, "de",lugarTrabajo)
print("Su cheque en pesos es de: $"+str(resultado))
