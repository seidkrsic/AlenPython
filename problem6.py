

# 

def purple_shell(racers):
    x = racers[0] # prije promijene sacuvam ga u x
    racers[0]=racers[-1]   # ovdje prvi postaje zadnji
    racers[-1] = x # zadnji postaje prvi
    return racers




lista = ["Alen", "Deno", "Sejo"]
result = purple_shell(lista)
print(result)