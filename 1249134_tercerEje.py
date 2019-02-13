#función para convertir una tupla a mayusculas
#se recibe en str debido que asis e le pidio al usuario
def mayu(oracion):
    palabraM = ()
    for i in range(0,len(oracion)):
        #lo que se hace es que se va concatenando la tupla con la letra en mayuscula
        #como una tupla no se puede concatenar con un str hacemos un "cast" con tuple()
        palabraM = palabraM + tuple(oracion[i].upper())
    return palabraM

palabra = input("Ingrese una oración: ")
#aqui pasa lo mismo que la funcion solo que viceversa por lo que se convierte de nuevo a str
print("Oración en mayusculas y en forma tupla: " + str(mayu(palabra)))