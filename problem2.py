
# 2 

# print(10//3) # // cjelobrojno dijeljenje 

# print(10 % 3 ) # ostatak pri dijeljenju 

def to_smash(total_candies):
    return total_candies % 3 

n = int(input("Unesi broj cokoladica: ")) 
result = to_smash(n) 
print(result) 
