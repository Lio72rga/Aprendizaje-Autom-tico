#Determinación de signo de un número
#Escribe un programa que solicite un número al usuario y determine
# si es positivo, negativo o cero, mostrando el resultado correspondiente
# Solicitar el número al usuario
numero = float(input("Por favor, ingresa un número: "))

# Determinar el signo del número
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")