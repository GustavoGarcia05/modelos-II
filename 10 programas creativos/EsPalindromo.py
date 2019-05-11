def verificar(cadena):
        
        palabra=cadena
        palabra=palabra.lower()
        palabra=palabra.replace(" ","")
        palindromo = palabra[::-1]
        
        if palindromo==palabra:
            print ("Es un Palindromo")
        else:
            print ("No es un Palindromo")
    

verificar(input("Ingrese una palabra:\n "))
