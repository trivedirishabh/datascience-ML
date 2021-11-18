#NumPy Basics

import numpy as np

my_list = [1,2,3]

# Conversion of list to array

arr = np.array(my_list)
print(arr)

# conversion of nested list to matrix
my_mat = [[1,2,3],[4,5,6],[7,8,9]]
matr = np.array(my_mat)
print(matr)

# creating array using arange method
print(np.arange(0,10))

#creating matrix of zeros
print(np.zeros((5,5)))

#creating matrix of linearly spaced integers
print(np.linspace(0,5,10))

#creating identity matrix
print(np.eye(4))

#creating vector of random integers
print(np.random.rand(5))

#creating matrix of random integers
print(np.random.rand(5,5))

rnarr = np.random.randint(0,50,10)
print(rnarr)
#finding max and min integers

print(rnarr.max())
print(rnarr.min())

#finding index position of max and min integers
print(rnarr.argmax())
print(rnarr.argmin())