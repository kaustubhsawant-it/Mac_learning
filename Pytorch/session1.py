import torch as t

#Scalars, vectors & matrices
a = t.tensor(2.0) #scalar
b = t.tensor([1.0,2.0]) #vector
c = t.tensor([[1,2],[3,4]]) #Matrices

#Random and zeros
rand = t.rand(3,3)
zeros = t.zeros(2,3)
ones = t.ones(3,1)


print(f'''
A:{a}
B:{b}
C:{c}
Random Matrix: 
    {rand}
zero Matrix: 
    {zeros}
One Matrix: 
    {ones}
''')

#GPU Support test of Pytorch
print(t.cuda.is_available())  # Will return False on Mac
print(t.backends.mps.is_available())
print(t.device("cpu"))