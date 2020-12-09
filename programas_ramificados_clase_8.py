def players(my_age, bbf_age):
    # función (con parametros)
    if (my_age < bbf_age) == True:
        # si mi edad es menor que la de mi mejor amigo y esto es verdadero
        print("Tu mejor amigo es más viejito que tú.")
        # imprime el mensaje
    elif (my_age > bbf_age) == True:
        # si mi edad es mayor que la de mi mejor amigo y esto es verdad
        print("Tú eres más viejito que tu mejor amigo.")
        # imprimir mensaje
    elif (my_age == bbf_age) == True:
        # si mi edad es igual que la de mi mejor amigo y esto es verdad
        print("Tú y tu mejor amigo tienen la misma edad.")
        # imprime mensaje
    else:
        print("sepa la tostada")
        # si ninguna de las anteriores es imprime mensaje


def run():
    # Función
    print("Conoce quien es más grande, tú o tu mejor amigo.")
    print("")
    # Impresión en pantalla para bienvenida

    my_age = int(input("¿Cuantos años tienes?"))
    # Pregunta al usuario convertida en entero
    bbf_age = int(input("¿Cuantos años tiene tu mejor amigo?"))
    #Pregunta al usuario convertida a entero

    result = players(my_age, bbf_age)
    # resultado de la función (parametros)


if __name__ == "__main__":
    run()
    # Entry point