# Ufuncs help in vectorization of arrays
# %% Without Ufuncs:
import numpy as np
# Adding two elements of a list
# Using zip():
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
print(z)
# %% Creating your own Ufuncs
import numpy as np
# Create your own ufunc:
def myadd(x, y):
  return x + y

myadd = np.frompyfunc(myadd, 2, 1) # frompyfunc(function, number of input arguments, number of output arguments)
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))
# Checking whether a function is a ufunc
import numpy as np
x = np.add(1, 1)
print(x)
print(type(x)) # It should print <class 'numpy.ufunc'> 
# %% Arithmetic operations on arrays
import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
arr=np.array([-1, -2, -3, -4, -5, -6])

newarr=np.add(arr1, arr2) # Addition
print(newarr)
newarr=np.subtract(arr1,arr2) # Subtraction
print(newarr)
newarr=np.multiply(arr1,arr2) # Multiplication
print(newarr)
newarr=np.divide(arr1,arr2) # Division
print(newarr)
newarr=np.power(arr1,arr2) # Power
print(newarr)
newarr=np.mod(arr1,arr2) # Modulus
print(newarr)
newarr=np.divmod(arr1,arr2) # Returns both quotient and remainder in two different arrays
print(newarr)
newarr=np.absolute(arr) # We don't use abs() as we could get confused with the abs() function in math module. 
print(newarr)
# %% Rounding off
import numpy as np
arr=np.array([-1.1, -1.9, 1.1, 1.9])
newarr=np.around(arr) # Rounds off to the nearest integer
print(newarr)
newarr=np.floor(arr) # Rounds off to the nearest lower integer
print(newarr)
newarr=np.ceil(arr) # Rounds off to the nearest upper integer
print(newarr)
newarr=np.trunc(arr) # Truncates decimals
print(newarr)
newarr=np.fix(arr) # Truncates decimals
print(newarr)
# %% Logarithms - Numpy gives us logs to 2,e and 10
import numpy as np
arr=np.array([1, 2, 3, 4, 5, 6])
newarr=np.log(arr) # Log base e
print(newarr)
newarr=np.log2(arr) # Log base 2
print(newarr)
newarr=np.log10(arr) # Log base 10
print(newarr)
# To calculate logarithm wrt any base, we use a frompyfunc() and import math module
import numpy as np
import math
arr=np.array([1, 2, 3, 4, 5, 6])
def mylog(x):
  return math.log(x)

mylog = np.frompyfunc(mylog, 1, 1)
print(mylog(arr))
# %% Summations
import numpy as np
arr1=np.array([1, 2, 3, 4, 5, 6])
arr2=np.array([2, 3, 4, 5, 6, 7])
newarr=np.sum([arr1,arr2]) # Sum of all elements
print(newarr)
newarr=np.sum([arr1,arr2], axis=1) # Sum of all elements in each row
print(newarr)
newarr=np.sum([arr1,arr2], axis=0) # Sum of all elements in each column
print(newarr)
newarr=np.cumsum(arr1) # Cumulative sum
print(newarr)
# %% Products
import numpy as np
arr1=np.array([1, 2, 3, 4, 5, 6])
arr2=np.array([2, 3, 4, 5, 6, 7])
newarr=np.prod([arr1,arr2]) # Product of all elements
print(newarr)
newarr=np.prod([arr1,arr2], axis=1) # Product of all elements in each row
print(newarr)
newarr=np.prod([arr1,arr2], axis=0) # Product of all elements in each column
print(newarr)
newarr=np.cumprod(arr1) # Cumulative product
print(newarr)
# %% Differences
import numpy as np
arr1=np.array([1, 2, 3, 4, 5, 6])
arr2=np.array([2, 3, 4, 5, 6, 7])
newarr=np.diff(arr1) # Difference of all elements
print(newarr)
newarr=np.diff(arr1, n=2) # Difference of all elements n times
print(newarr)
# %% LCM and GCD
import numpy as np
arr1=np.array([1, 2, 3, 4, 5, 6])
arr2=np.array([2, 3, 4, 5, 6, 7])
newarr=np.lcm.reduce(arr1) # LCM of all elements
print(newarr)
newarr=np.gcd.reduce(arr2) # GCD of all elements
print(newarr)
# %% Trigonometry
import numpy as np
arr=np.array([0, np.pi/2, np.pi])
newarr=np.sin(arr) # Sine of all elements
print(newarr)
newarr=np.cos(arr) # Cosine of all elements
print(newarr)
newarr=np.tan(arr) # Tangent of all elements
print(newarr)
newarr=np.arcsin(arr) # Arcsine of all elements
print(newarr)
newarr=np.arccos(arr) # Arccosine of all elements
print(newarr)
newarr=np.arctan(arr) # Arctangent of all elements
print(newarr)
arr = np.array([90, 180, 270, 360]) # Degrees to radians
x = np.deg2rad(arr)
print(x)
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi]) # Radians to degrees
x = np.rad2deg(arr)
print(x)

# %% Hyperbolic functions
import numpy as np
arr = np.array([0.1, 0.2, 0.5])
newarr = np.sinh(arr)
print(newarr)
newarr = np.cosh(arr)
print(newarr)
newarr = np.tanh(arr)
print(newarr)
newarr = np.arcsinh(arr)
print(newarr)
newarr = np.arccosh(arr)
print(newarr)
newarr = np.arctanh(arr)
print(newarr)
# %% Set operations
import numpy as np
arr=np.array([1,2,3,3,3,4,4,4,5,5,6,6,6,7,7,8,8,8,9,9]) # Returns unique elements
print(np.unique(arr))

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.intersect1d(arr1, arr2, assume_unique=True) # Intersection of two arrays
print(newarr)
newarr = np.union1d(arr1, arr2) # Union of two arrays
print(newarr)
newarr = np.setdiff1d(arr1, arr2, assume_unique=True) # Difference of two arrays
print(newarr)
newarr = np.setxor1d(arr1, arr2) # XOR of two arrays
print(newarr)