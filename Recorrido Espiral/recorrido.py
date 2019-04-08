# https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html

def leerArchivo():
    return[x.split() for x in open("matriz.txt").readlines()]

def moverDerecha(matriz,x,y,centinela,longitud):
    if(centinela<longitud):
        print(matriz[x][y],end=" ")
        moverDerecha(matriz,x,y+1,centinela+1,longitud)
    if(centinela==longitud):
        moverAbajo(matriz,x+1,y-1,0,longitud-1)

def moverAbajo(matriz,x,y,centinela,longitud):
    if(centinela<longitud):
        print(matriz[x][y],end=" ")
        moverAbajo(matriz,x+1,y,centinela+1,longitud)
    if(centinela==longitud):
        moverIzquierda(matriz,x-1,y-1,0,longitud)

def moverIzquierda(matriz,x,y,centinela,longitud):
    if(centinela<longitud):
        print(matriz[x][y],end=" ")
        moverIzquierda(matriz,x,y-1,centinela+1,longitud)
    if(centinela==longitud):
        moverArriba(matriz,x-1,y+1,0,longitud-1)

def moverArriba(matriz,x,y,centinela,longitud):
    if(centinela<longitud):
        print(matriz[x][y],end=" ")
        moverArriba(matriz,x-1,y,centinela+1,longitud)
    if(centinela==longitud):
        moverDerecha(matriz,x+1,y+1,0,longitud)

moverDerecha(leerArchivo(),0,0,0,len(leerArchivo()))
        

    
