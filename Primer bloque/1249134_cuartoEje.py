def mayu(oracion):
    palabraM = ()
    for i in range(0,len(oracion)):
        #lo que se hace es que se va concatenando la tupla con la letra en mayuscula
        #como una tupla no se puede concatenar con un str hacemos un "cast" con tuple()
        palabraM = palabraM + tuple(oracion[i].upper())
    return palabraM

def strToLis(palabra):
    lista = []
    for i in range(0,len(palabra)):
        lista.append(palabra[i])
    return lista


palabra = 'ejemplo'
print('Palabra a convertir: '+palabra)
print('Palabra en forma de lista: '+ str(strToLis(palabra)))
print('Palabra en forma de Mayusculas: ' + str(mayu(list(strToLis(palabra)))))