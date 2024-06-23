





# # PROMJENLJIVE 

# a = 12 # int 
# b = 10 
# c = a + b 
# # * - puta 
# # / - dijeljenje 
# # ** - stepen ....  a**2 = a ^ 2 


# # STRING 
# string_value = "python" 
# a = "1."
# b = "2" 

# print(a*3)   # mnozenje stringa brojem 

# # PRINT 

# # 1.2 - float tip podataka - decimalan broj 

# # print("Alen", "Novalic", 1, 2, "Python", 1.2)   


# # round(broj, decimale)

# print(round(1/3, 2))    

# # BOOLEAN  TRUE or FALSE 

# x = 8
# y = False 


# # if 
# # if x < 10:  
# #     print("Alen")
# # elif x > 10:
# #     print("Denis") 
# # else: 
# #     print("Sejoo")  

# #    0 1 2   3       4     5     6 
# l = [1,2,3, "Alen", True, 1.2, [1,2,3]]  
# pod_lista = l[6]
# print(pod_lista[0]) 


# # 
#   int ("10")  --- > 10 
#                                 # int ("cat") --- > akjflkak
# n = int(input("Unesi broj: ")) 

# # for i in range(1,n+1):  
# #     print(i, "Hello") 
# # range(1,11) --- > [1,2,... 10]
# for i in [1,2,3, 4,5,6]: 
#     print(i)
 


class Dog: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

    def aw(self): 
        for _ in range(10):
            print("Alen") 

# string = "sejo" 
# print(len(string)) 

matrix = [[1,2,3,3], 
          [4,5,6, 3], 
          [7,8,9, 3],
          [1,1,1,1],
        ]

dimenzija = len(matrix) 

for i in range(dimenzija): # i = 0 
    for j in range(4): # j = 0,... 3 
        if i != j: 
            matrix[i][j] = 1 

# for i in range(4):
#     print(matrix[i])




# FUNKCIJE 

def funkcija():
    for _ in range(3):
        print("Hello")  


def zbir(x, y):  # f(x,y) = x + y 
    return x + y 


def hello(to):  
    print("Hello", to)

# print("alkfldk")
# x = zbir(2,3)
# print(x + 1) 
"""
klajdfkj
aldfma,
adkfj
"""

def zbir1(x, y): 
    x = x ** 2 
    y = y ** 3 
    return zbir(x,y) , "Hello"   

x , y = 1, 2 

result, name = zbir1(2,3) 
print(result)   


def sejo(): 
    pass 