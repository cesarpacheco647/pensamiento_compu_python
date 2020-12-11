def ages (my_name, my_age, bff_name, bff_age):
    # función (con parametros) (Se agragaron 2 parametros mas un total de 4 parametros)
    if (my_age < bff_age) == True:
        # si mi edad es menor que la de mi mejor amigo y esto es verdadero
        print(f"Tu mejor amigo {bff_name} es más viejito que tú.")
        # imprime el mensaje con f-strigns
    elif (my_age > bff_age) == True:
        # si mi edad es mayor que la de mi mejor amigo y esto es verdad
        print(f"Tú {my_name} eres más viejito que tu mejor amigo.")
        # imprimir mensaje con f-strigns
    elif (my_age == bff_age) == True:
        # si mi edad es igual que la de mi mejor amigo y esto es verdad
        print(f"Tú {my_name} y tu mejor amigo {bff_name} tienen la misma edad.")
        # imprime mensaje con f-strigns
    else:
        print("sepa la tostada")
        # si ninguna de las anteriores es imprime mensaje


def run():
    # Función
    print("Conoce quien es más grande, tú o tu mejor amigo.")
    print("")
    # Impresión en pantalla para bienvenida

    my_name = input("¿Cómo te llamas?")
    my_age = int(input("¿Cuantos años tienes?"))
    # Pregunta al usuario convertida en entero
   
    bff_name = input("¿Cómo se llama tu mejor amigo?")
    bff_age = int(input("¿Cuantos años tiene tu mejor amigo?"))
    #Pregunta al usuario convertida a entero

    result = ages(my_name, my_age, bff_name, bff_age)
    # resultado de la función (parametros)


if __name__ == "__main__":
    run()
    # Entry point