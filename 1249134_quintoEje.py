def numPar(lista):
    listaP=[]
    for i in range(0, len(lista)):
        if (i+1)%2 == 0:
            listaP.append(lista[i])
    return listaP

salida = 's'
lista = []
while salida != 'n':
    lista.append(int(input("Ingrese un numero: ")))
    salida = input("Quiere agregar otro numero? (s/n)")
print("Lista original: " + str(lista))
print("lista con numeros en posicion par: " + str(numPar(lista)))
