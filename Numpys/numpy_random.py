# %% Dealing with random values
from numpy import random
x=random.rand() # Returns a random float between 0 and 1
print(x)
x=random.randint(100) # Returns a random integer between 0 and 100
print(x)
x=random.randint(100, size=(5)) # Returns a 1-D array of size 5 with elements between 0 and 100
print(x)
x=random.randint(100, size=(3,5)) # Returns a 2-D array of size 3x5 with elements between 0 and 100
print(x)
x=random.choice([3,6,9]) # Returns a random element from the list
print(x)
x=random.choice([3,6,9], size=(3,5)) # Returns a 2-D array of size 3x5 with elements from the list
print(x)
# %% Random Distributions
from numpy import random
import numpy as np
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(10))
print(x) # We assigned probabilities for every element in the list. All the probabilities should add up to 1.

arr=np.array([2,3,4,5,6,7])
print(random.permutation(arr)) # Doesn't change the array

random.shuffle(arr)
print(arr) # Changes the array