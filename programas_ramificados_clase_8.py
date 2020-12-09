def players(my_age, bbf_age):
    if my_age < bbf_age:
        print("Tú eres más viejo que tu mejor amigo")
    elif bbf_age > my_age:
        print("Tu mejor amigo es más viejito que tú")
    elif my_age == bbf_age:
        print("tienen la misma edad")
    else:
        print("sepa la tostada")


def run():
    print("Conoce quien es más grande, tú o tu mejor amigo.")
    print("")

    my_age = int(input("¿Cuantos años tienes?"))
    bbf_age = int(input("¿Cuantos años tiene tu mejor amigo?"))

    result = players(my_age, bbf_age)

    


if __name__ == "__main__":
    run()