#funcion que invierte la lista
def rev(lista):
    reversa = []
    #el ciclo empieza en el ultimo elemento de la lista, para ir decrementando mientras sea mayor a -1
    for i in range(len(lista)-1, -1, -1):
        reversa.append(lista[i])
    return reversa

lista1=[]
listaR=[]
bandera = 's'
#se empiezan a tomar datos mientras que el usuario quiera
while bandera == 's':
    lista1.append(int(input("Introdusca un numero:")))
    bandera = input("Quieres ingresar otro? (s/n)")
listaR=rev(lista1)
print("Lista original: "+ str(lista1))
print("Lista inversa: "+ str(listaR))