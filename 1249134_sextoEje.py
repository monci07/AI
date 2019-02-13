def pickInd(lista, indices):
    listaN = []
    j=0
    for i in range(0,len(lista)):
        if i == indices[j]:
            j+=1
            listaN.append(lista[i])
        if j == len(indices):
            break
    return listaN

lista = []
indices = []
aux = 0
print("Ingrese una serie de numeros presionando enter entre ellos: (ingrese una 's' para indicar que acabo)")
while aux != 's':
    aux=input()
    if aux.isdigit() == True:
        lista.append(int(aux))
    else:
        break
print('')
print('De la misma manera indique los indices que desea rescatar de la lista anterior: (misma instrucción)')
while aux != 's':
    aux=input()
    if aux.isdigit() == True:
        indices.append(int(aux))
    else:
        break
print('')
print('Lista de numeros inicial: ' + str(lista))
print('Lista de indices: ' + str(indices))
print('Lista de los numeros rescatados: ' + str(pickInd(lista,indices)))