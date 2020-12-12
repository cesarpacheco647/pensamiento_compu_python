contador_externo = 0
# variable 1
contador_interno = 0
# variable 2

while contador_externo < 5:
    # mientras el contador externo sea menor a 5
    while contador_interno < 6:
        # mientras el contador interno se menor a 6
        #  se cumple las dos 
        print(contador_externo, contador_interno)
        # imprime las variables
        contador_interno += 1 #contador = contador + 1
        # suma 1 al contador para que el numero cambie
        if contador_interno >= 3:
        # Si el contador interno es menor a 3
            break
            # ¡Para!
            
    contador_externo += 1
    # suma 1 al contador para que el numero cambie
    contador_interno = 0
    # reseteamos el contador por que sino solo correria una vez