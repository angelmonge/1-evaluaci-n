def condicional_2():
    edad=input("cual es tu edad? ")
    if(edad >= 18 ):
        print "Sala alcoholica "
    else:
        if(edad >= 15 ):
            print "Sala adoescentes"
        else:
            print "Sala infantil"

condicional_2()
