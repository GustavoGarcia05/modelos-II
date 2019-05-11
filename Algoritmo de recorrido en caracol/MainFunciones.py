def leerArchivo():
    return[x.split() for x in open("matriz.txt").readlines()]

def imprimir(lista):
    print (" ".join(lista), end=" ")

def girar(lista):
    return [[fila[i] for fila in lista] for i in reversed(range(len(lista[0])))]

def recorrer(lista):
    imprimir(lista[0])
    lista.pop(0)
    if len(lista)>0:
        recorrer(girar(lista))
   
lista = leerArchivo()
recorrer(lista)

