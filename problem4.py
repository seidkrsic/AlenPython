


def suma(x): # x = [1,2,300, 4,5, 6] .... x[0] = 1 x[2] = 300 
    suma1 = 0
    for i in range(0,len(x)):
        if x[i] > 100:  # sabrali sve brojeve vece od 100, inace ih preskocili 
            suma1 = suma1 + x[i] 
    return suma1 

lista = [1, 2, 300, 40, 500, 600]
print(suma(lista))


# for i in range(0, len(lista)): 
#     print("Index", i) 
#     print("Vrijednost lista[i]", lista[i]) 