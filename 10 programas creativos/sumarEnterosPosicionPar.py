def sumar(lista):
    suma=0
    for i in range(0,len(lista),2):
        if(lista[i]%1==0):
            suma+=lista[i]
    return suma

print (sumar([1,2,3,4,5]))
    
