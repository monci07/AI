#función que detecta si un numero es primo o no
def primo(num):
    aux=0
    # el ciclo va dividiendo los numeros anteriores con el numero proporcionando y si da un resultado diferente a 0 aumenta el contador
    for i in range(2,num+1):
        if (num % i) != 0:
            aux+=1
    # el contador se compara con el numero dado menos dos
    # el -2 es por que el contador empieza desde el dos.
    if aux==num-2:
        return True
    else:
        return False
    

def listaPri(num):
    lista = []
    for i in range(2,num):
        if primo(i) == True:
            lista.append(i)
    return lista

lista = []
num = int(input("Introduzca un numero mayor a 2:"))
lista.extend(listaPri(num))
print(str(lista))