def bucle_11():
    #Suma de numeros pares e impares
    nfinal= input("Hasta que numero quieres sumar: ")
    #definimos variable para sumar los pares
    suma_pares=0 #inicializamos la variable a cero
    #definimos la variable para sumar los impares
    suma_impares=0 #inicializamos la variable a cero
    for numero in range(1,nfinal+1):
        #para cada numero me pregunto si es par o impar
        if(numero%2==0):
            print str(numero)," es par"
            suma_pares=suma_pares+numero
        else:
            print str(numero), " es impar"
            suma_impares=suma_impares+numero
    print "La suma de los numeros pares vale",suma_pares
    print "La suma de los numeros impars vale",suma_impares

bucle_11()
