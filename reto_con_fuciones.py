def enumeraciones():
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

def aproximaciones():
    objetivo = int(input('Escoge un numero: '))
    # Pedimos el número al usuario
    epsilon = 0.0001
    # que tan cerca queremos llegar a la respuesta
    paso = epsilon**2 
    # que tanto nos vamos a ir acercando en cada iteracion 
    respuesta = 0.0
    # tendrá la respuesta al finalizar las iteraciones

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        # condicion (nos dice que cada vez mas nos estamos acercando al objetivo)
        # que llegemos al valor de epsilon 
        # and en este caso nos protege contra número negativos
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso
        # en cada iteración le sumas el paso a la respuesta

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
        # checamos si llegamos a la solucion se lo decimos al usuario
    else:
        print(f'La raiz cudrada de {objetivo} es {respuesta}')
        # sino llegamos a la solucion tambien se lo decimos al usuario

def binaria():
    objetivo = int(input('Escoge un numero: '))
    # pedimos un numero al usuario
    epsilon = 0.001
    # que tan preciso deseamos que sea
    bajo = 0.0
    # limite inferior
    alto = max(1.0, objetivo)
    # max nos regresa el valor mas alto entre dos valores
    # regresandos 1.0 o el objetivo (si el objetivo es menor a 1.0 empezamos en 1.0)
    respuesta = (alto + bajo) / 2
    # dividimos entre 2 el alto y el bajo

    while abs(respuesta**2 - objetivo) >= epsilon:
        # utilizamos al funcion abs para encontrar valores absolutos
        # absolute value (abs)
        # la respuesta al cuadrado menos el objetivo tiene que ser mayor o igual a epsilon
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        # viendo que está pasando dentro del codigo
    if respuesta**2 < objetivo:
        # si la respuesta al cuadrado es menor que objetivo
        bajo = respuesta
        # entonces bajo es nuestra nueva respuesta
    else:
        # de lo contrario
        alto = respuesta
        # alto es nuestra nueva respuesta
        # aqui definimos si nos vamos para arriba o para bajo los valores 
        # (haciendo mas pequeño la busqueda)
        # redefinimos que es bajo y que es alto
        respuesta = (alto + bajo) / 2
        # volvemos la respuesta cada vez mas pequeña (al dividirla entre dos) 
        # por eso es busqueda binaria

    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    # imprimimos la respuesta

def run():
    print("""Bienvenido al reto con fuciones del curso de pensamiento computacional con python de platzi. 

    En este reto vamos a poder encontrar la raiz cudadrada de culquier número, pero... 
    para hacerlo podras elegir una de las tres opciones siguientes: 
    """)
    # bienvenida

    selection = int(input("""Escribre:
    1 para realizar con enumeraciones
    2 para aproximaciones 
    3 para busqueda binaria

    """))
    # seleccion de opcion
    
    if selection == 1:
        # si se selecciono la opción 1
        enumeraciones()
        # ejecuta la funcion enumeraciones
    elif selection == 2:
        # si se selecciono la opción 2
        aproximaciones()
        # ejecuta la funcion aproximaciones
    elif selection == 3:
        # si se selecciono la opción 3
        binaria()
        # ejecuta la funcion binaria
    else:
        # si ninguna de las anteriores haz...
        print("sepa Dios que pasó")

if __name__ == "__main__":
    run()
    # entry point