
#Promedio de Edades por Grupo
#Escribe una función que solicite al usuario ingresar edades de personas.
#Finalizar la entrada de datos con la palabra "Salir". Luego, muestra 
# el promedio de edades de los mayores de edad (18 años o más) y el 
# promedio de edades de los menores de edad.
def promedio_edades():
    # Listas para almacenar las edades de mayores y menores de edad
    mayores = []
    menores = []

    while True:
        # Solicitar la edad del usuario
        entrada = input("Ingresa una edad (o Escriba 'Salir' para terminar): ")
        
        # Verificar si se debe terminar la entrada de datos
        if entrada.lower() == 'salir':
            break

        # Convertir la entrada a un número entero
        try:
            edad = int(entrada)
            if edad >= 18:
                mayores.append(edad)
            else:
                menores.append(edad)
        except ValueError:
            print("Por favor, ingresa un número válido o escriba 'Salir' para terminar.")

    # Calcular el promedio de edades de mayores y menores de edad
    if mayores:
        promedio_mayores = sum(mayores) / len(mayores)
    else:
        promedio_mayores = 0

    if menores:
        promedio_menores = sum(menores) / len(menores)
    else:
        promedio_menores = 0

    # Mostrar los resultados
    print(f"Promedio de edades de mayores de edad es: {promedio_mayores:.2f}")
    print(f"Promedio de edades de menores de edad es: {promedio_menores:.2f}")

# Llamar a la función para ejecutar el programa
promedio_edades()

{
    "languaje": "es",
    "words": []
}