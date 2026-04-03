#Función para doblar un número
#Escribe una función que reciba un número y devuelva su doble. 
# Luego, solicita un número al usuario y muestra el resultado 
# utilizando la función.
# Definir la función que dobla un número
def doblar_numero(numero):
    return numero * 2

# Solicitar un número al usuario
numero_usuario = float(input("Por favor, ingresa un número: "))

# Utilizar la función para doblar el número
resultado = doblar_numero(numero_usuario)

# Mostrar el resultado
print(f"El doble de {numero_usuario} es {resultado}.")