



def to_smash(total_candies, num_of_friends):
    return total_candies % num_of_friends



n = int(input("Unesi broj cokoladica"))
m = int(input("Unesi broj prijatelja"))
result = to_smash(n, m)

print(result)