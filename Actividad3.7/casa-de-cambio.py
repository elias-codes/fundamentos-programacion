# Este programa cambia el cheque de los trabajadores 
# de pesos a dolares y cobra una comision de 70 MXN
tipoDeCambio = 19.5
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

# Solicitamos el nombre y lugar de trabajo al 

nombreCliente = input("Favor de introducir su nombre: ")
lugarTrabajo = input("Favor de introducir su lugar de trabajo")

# Aqui solicitamos la cantidad de dolares a cambiar

dolares = int(input("Introduzca los dolares de su cheque"))

# Convertimos la cantidad a pesos y restamos la comision