import numpy as np

def creaMat(dim, val):
    mat1= np.random.randint(low=val[0],high=val[1], size=dim)
    mat2= np.random.randint(low=val[0],high=val[1], size=dim)
    print("Matriz 1: ")
    print(str(mat1))
    print("Matriz 2: ")
    print(str(mat2))
    print("Resultado: ")
    print(str(np.dot(mat1,mat2)))

dim = ()
val = ()

print("Ingrese las dimenciones de las matrices: ")
dim = (int(input("Renglones: ")),)
dim = dim + (int(input("Columnas: ")),)
print("Ingrse los rangos de los valores dentro de las matrices: ")
val = (int(input("Min: ")), )
val = val + (int(input("Max: ")),)

creaMat(dim,val)