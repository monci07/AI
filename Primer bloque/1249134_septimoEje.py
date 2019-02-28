def primo(num):
    aux=0
    for i in range(2,num+1):
        if (num % i) == 0:
            aux+=1
    if aux==1:
        return True
    else:
        return False

def listaPri(num):
    lista = []
    for i in range(2,num+1):
        if primo(i) != True:
            lista.append(i)
    return lista

num = int(input("Ingrece un numero: "))
lista = listaPri(num)
print(str(lista))