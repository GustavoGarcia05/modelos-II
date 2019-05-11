def busquedaBinaria(lista,item):
    
    
    if(len(lista)==0):
        return False
    else:
        if(item==lista[len(lista)//2]):
            return True
        else:
            if(item<lista[len(lista)//2]):
                return busquedaBinaria(lista[:len(lista)//2],item)
            else:
                return busquedaBinaria(lista[(len(lista)//2)+1:],item)

print(busquedaBinaria(range(100),int(input("Metalo socio: \n"))))
