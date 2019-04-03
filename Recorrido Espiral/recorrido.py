# https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html

def leerArchivo():
    return[x.split() for x in open("matriz.txt").readlines()]

def leerLinea():
    print(leerArchivo())
    print('------------------------')
    print(leerArchivo()[slice(-1)])
    print('------------------------')
    
    
leerLinea()    

    
