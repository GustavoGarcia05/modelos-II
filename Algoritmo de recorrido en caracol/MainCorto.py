def recorrer(lista):
    print (" ".join(lista[0]), end=" ")
    lista.pop(0)
    if len(lista)>0:
        recorrer([[fila[i] for fila in lista] for i in reversed(range(len(lista[0])))])

recorrer([x.split() for x in open("matriz.txt").readlines()])

