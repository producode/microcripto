def corrimientoDeLetra(palabra,movimiento,cantidadMaximaCorrimiento):
    palabraNueva = ""
    for letra in palabra:
        asciiLetra = ord(letra)
        if(asciiLetra >= 90 and asciiLetra < 97):
            asciiLetra = 64
        elif(asciiLetra >= 122):
            asciiLetra = 97
        if(cantidadMaximaCorrimiento != 0):
            while((asciiLetra+movimiento) > (65 + cantidadMaximaCorrimiento) and asciiLetra < 97):
                asciiLetra -= cantidadMaximaCorrimiento
            while ((asciiLetra + movimiento) > (97 + cantidadMaximaCorrimiento)):
                asciiLetra -= cantidadMaximaCorrimiento
        asciiLetra = movimiento + asciiLetra
        palabraNueva += chr(asciiLetra)
    return palabraNueva

#http://www.robindavid.fr/blog/2012/06/15/kasiski-babbage-cryptanalysis-in-python/
def getDivisores(nro):
    divisores = []
    for nroDivisor in range(2,nro):
        if nro % nroDivisor == 0:
            divisores.append(nroDivisor)
    return divisores


def getTuples(l):
    frecuencia =[]
    cantidad = 0
    i = 0
    while i < len(l): # Loop through all the list
        elt= l[i:i+3] # Take at least 3-character length for tuples
        long = len(elt)
        if long == 3: #should be 3 if not means we are at the end of the list
            for j in range(i+1,len(l)): #Find further in the list for the same pattern
                if l[i:i+long] == l[j:j+long]: #If match the 3-char check for more
                    while l[i:i+long] == l[j:j+long]:
                        long = long + 1
                    long = long -1
                    elt = l[i:i+long] # Now we have a tuple
                    diff = j - i # Compute the distance
                    frecuencia.extend(getDivisores(diff)) #Add the divisors to the list
                    print ("%s\ti:%s\tj:%s\tdiff:%s\t\tDivisors:%s" % (elt,i,j, diff,getDivisores(diff))) #Print information about the tuple (can be deleted)
                    cantidad = cantidad +1
                    j = j + long + 1
            i = i + long -3 +1
        else:
            i = i + 1
    return cantidad, frecuencia

def analisisFrecuencia(palabra):
    arrayParaAnalisis = []
    for letra in palabra:
        arrayParaAnalisis.append(ord(letra))
    return getTuples(arrayParaAnalisis)

palabra = str(input("ingrese la palabra: "))
mover = int(input("ingrese el corrimiento: "))
cantidadMaximaCorrimiento = int(input("ingrese un maximo de corrimiento (0 para no utilizar): "))
print(corrimientoDeLetra(palabra,mover,cantidadMaximaCorrimiento))
cantidad, frecuencia = analisisFrecuencia(palabra)
print(cantidad)
print(frecuencia)