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