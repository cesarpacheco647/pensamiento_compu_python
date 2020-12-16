objetivo = int(input('Escoge un entero: '))
# introducir cantidad
respuesta = 0
# contador

while respuesta**2 < objetivo:
    # mietras la respuesta al cuadrado (**) sea menor que el objetivo
    print(respuesta)
    # solo para ver que esta pasando dentro de este ciclo
    respuesta += 1
    # aumenta 1 (evitando el infinite loop)

if respuesta**2 == objetivo:
    # si la respuesta al cuadrado (**) es igual al objetivo
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    # imprimimos mensaje
else:
    # sino
    print(f'{objetivo} no tiene una raiz cuadrada exacta')
    # imprimimos mensaje