


import numpy as np


niz = np.array([[1,2,3],[4,5,6]])      

# print(niz.ndim) 

# print(niz.shape)
# print(niz.dtype) 
# print(niz.size)   

# print(niz[1,1]) 
# print(niz[0, : ]) 
# print(niz[:, 0])   


# a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]]) 
# a[0,0] = 100 
# a[:, 2] =  [200,200] 
# print(a) 
# print(a[1, 1 : : 2]) 
 
# niz = np.zeros((2,2), dtype="int32")   # dtype="float32"

# niz2 = np.ones((2,2), dtype="int32") 
# print(niz2)  

# niz3 = np.full((2,2), 99, dtype="int32") 
# niz3[0,0] = 23
# print(niz3)  
             
# niz4 = np.random.randint(1,10, size=(3,3)) 
# print(niz4) 

# niz5 = np.identity(3, dtype="int32")  
# print(niz5) 


# niz6 = np.array([[1], [2], [3]]) 
# r1 = np.repeat(niz6, 3, axis=1)  
# print(r1) 


# ones = np.ones((5,5), dtype="int32") 
# print(ones) 
# zeros = np.zeros((3,3), dtype="int32") 
# zeros[1,1] = 9  

# ones[ 1:4 , 1:4 ] = zeros

# print(ones)  



# niz = np.full((1,5), 9, dtype="int32") 
# niz1 = np.full((1,5), 10, dtype="int32") 
# print(niz + niz1)  
# a = np.ones((2,2), dtype="int32") 
# b = np.full((3,2), 2, dtype="int32")  
# # z = np.matmul(a,b)
# # print(z)  

# c = int(np.linalg.det(a))    
# print(c) 

# v1 = np.array([1,2,3,4]) 
# v2 = np.array([5,6,7,8]) 

# # print(np.vstack((v1,v2,v1,v2))) 
# print(np.hstack((v1,v2, v1)))     


# n = int(input("Unesi neki broj: ")) 
# lista = [] 
# for i in range(n): 
#     lista.append(np.arange(1,n+1))      # dodajemo na kraju liste novi element... za to sluzi append 

# # print(lista) 
# X = np.array(lista)   


# lista2 = [] 

# for i in range(n):
#     lista2.append(np.full(n, i+1, dtype="int32")) 

# Y = np.array(lista2) 

# print(X)
# print(Y)  


 

# unose se brojevi neparni n i k, n>k 
# matrica je dimenzija 2n+k x 2n+k 


n = int(input("Unesi n: "))
k = int(input("Unesi k: "))


niz1 = np.zeros((2*n+k, 2*n+k), dtype="int32") 

niz2 = np.full((k,k), 2, dtype="int32")
 
niz3 = np.ones((n, k), dtype="int32")

niz4 = np.ones((k,n), dtype="int32")

niz5 = np.ones((k,n), dtype="int32")

niz6 = np.ones((n,k), dtype="int32")


niz1[n:n+k,n:n+k] = niz2 
niz1[0:n, n:n+k] = niz3 
niz1[n:n+k, 0:n] = niz4
niz1[ n:n+k,n+k:2*n+k] = niz5
niz1[n+k:2*n+k, n:n+k] = niz6

print(niz1)  








