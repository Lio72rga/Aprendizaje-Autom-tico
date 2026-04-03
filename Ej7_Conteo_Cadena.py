#Conteo de letra en una cadena
#Escribe un programa que solicite una cadena de texto y una letra
# al usuario, y cuente cuántas veces aparece esa letra enla cadena,
# mostrando el resultado
# Solicitar una cadena de texto al usuario
cadena = input("Por favor, ingresa una cadena de texto: ")

# Solicitar una letra al usuario
letra = input("Por favor, ingresa una letra para contar: ")

# Contar cuántas veces aparece la letra en la cadena
conteo = cadena.count(letra)

# Mostrar el resultado
print(f"La letra '{letra}' aparece {conteo} veces en la cadena.")