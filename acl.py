numero = int(input("Ingrese número de la ACL: "))

if numero >= 1 and numero <= 99:
    print ("El número " + str(numero), "es de una ACL ESTANDAR")
elif numero >= 1300 and numero <= 1999:
    print ("El número " + str(numero), "es de una ACL ESTANDAR")
elif numero >= 100 and numero <= 199:
    print ("El número " + str(numero), "es de una ACL EXTENDIDA")
elif numero >= 2000 and numero <= 2699:
    print ("El número " + str(numero), "es de una ACL EXTENDIDA")
else:
    print ("El número " + str(numero), "no corresponde a una ACL")
