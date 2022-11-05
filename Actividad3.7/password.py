#Ese programa pide una contrasenia y la convierte en minusculas
definedPass = "lacontra"

#Pide la contrasena

contra = input("Favor de introducir la contrasena: ")

#convertimos a minusculas 

contra = contra.lower()

#verificamos si sean iguales

if definedPass == contra:
    print("Inicio exitoso")
else: 
    print("Escribe de nuevo la contrasena")