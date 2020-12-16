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