#filtrar lista con elementos > a limite

#def filtra_lista(lista,limite):
#    if not lista:
#        return []
    
#    else:
#        head,*tail = lista
#        if head > limite:
#            return [lista[0]] + filtra_lista(tail,limite)
#        else:
#            return filtra_lista(tail,limite)


#a = [1,2,3,4,5,6,7,8,9,10]

#print(filtra_lista(a,5))

##########################################################################################

#Invertir lista de objetos

#def invertir_lista(lista):
#    if not lista:
#        return []
    
#    else:
#        head,*tail = lista

#        return invertir_lista(tail) + [head]


#a = [1,2,3,4,5,6,7,8,9,10]

#print(invertir_lista(a))

########################################################################################

#Invertir una cadena

#def invertir_cadena(cadena):
#    if not cadena:
#        return ""
    
#    else:
#        head,*tail = cadena
#        return invertir_cadena(tail) + head


#a = "yo solo se, que nada se"

#print(invertir_cadena(a))

#######################################################################################

#fibonacci

def fibonacci(numero):
    lista_fib = []
    for i in range(0,numero,1):
        lista_fib.append(i)

    if not numero:
        return []
    
    else:
        head,*tail = lista_fib
        if head == 0 or head == 1:
            head = 1

        return fibonacci(tail[0]) + head



numero = 15
print(fibonacci(numero))