#Verificar si un texto que termina en punto es un palíndromo (capicúa). Un texto es palíndromo si se lee lo mismo de izquierda a derecha o de derecha a izquierda. Ej: “Amor a roma”.

def palindromo():

    texto=input("Verificar Palindromo:")
    texto = texto.replace(' ', '').lower()
    texto = texto.replace ('.','')

    if str(texto)==str(texto)[::-1]:
        print("Es un Palindromo")
    else:
        print("No es un Palindromo") 

    return(palindromo())      

print (palindromo())


   
