def primo(num):
    aux=0
    for i in range(1,num+1):
        if (num % i) == 0:
            aux+=1
    if aux==2:
        return True
    else:
        return False

def listaPri(num):
    lista = []
    for i in range(1,num+1):
        if primo(i) != True:
            lista.append(i)
    return lista

lista=listaPri(999999)
print(str(lista))