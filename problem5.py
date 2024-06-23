



def select_second(L):
    """
    vraca drugi element liste ako on postoji, a inace vraca None
    """
    if len(L) > 1: 
        return L[1]
    else:
        return None


lista = []  
result = select_second(lista)

print(result)