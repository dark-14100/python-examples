# %% Creating an array
import numpy as np
arr_list=np.array([10,20,30,40]) # Creating array using list
print(arr_list)
arr_tuple=np.array((10,20,30,40)) # Creating array using tuple
print(arr_tuple)

print(type(arr_list)) # A Numpy array's datatype is an ndarray
# %% Dimensions of an array
import numpy as np
# 0-D arrays
arr0=np.array(42)
# 1-D arrays
arr1=np.array([1,2,3,4,5])
# 2-D arrays
arr2=np.array([[1,2,3],[4,5,6]]) # Matrix
# 3-D arrays
arr3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[1,2,3]]])
# Check dimensions of array
print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
# %% Accessing array elements
import numpy as np
arr0=np.array(42)
arr1=np.array([1,2,3,4,5])
arr2=np.array([[1,2,3],[4,5,6]])
arr3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[1,2,3]]])

print([arr1[0]]) # Accessing first element in 1D array
print([arr2[1,2]]) # 2nd row, 3rd column 
print([arr3[0,1,2]]) # 3rd element of 2nd array of first array
# Think of it like a coordinate system, except that you need to -1 from every coordinate 
# %% Datatypes
import numpy as np

# Checking datatype
arr = np.array([1, 2, 3, 4])   
print(arr.dtype) # Returns i64

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype) # Returns U6

# Create arrays with specific datatype
arr = np.array([1, 2, 3, 4], dtype='S') # You can also define size. Example i4 - integer and 4 bytes
print(arr)
print(arr.dtype)

# Converting datatypes on existing arrays
arr1 = np.array([1.1, 2.1, 3.1])
newarr1 = arr1.astype('i')
print(newarr1)
print(newarr1.dtype) # i32

arr2=np.array([1,0,3])
newarr2=arr2.astype(bool)
print(newarr2)
print(newarr2.dtype) 
# %% Copy vs View
import numpy as np

# Copy
arr=np.array([1,2,3,4,5])
x=arr.copy()
y=arr.view()

x[0]=42
print(arr) # Nothing should change in first array
y[0]=42
print(arr) # First element should change in both arrays

# copies own the data. i.e. making changes to copies shouldn't change the original
# views don't own the data. They change the main attribute along with themselves

# Every NumPy array has the attribute base that returns None if the array owns the data. 
# Otherwise, the base attribute refers to the original object.
print(x.base)
print(y.base)

# %% Shape of an array
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)
# Output prints a tuple saying (2,4). Which means the array has 2 dimensions(cos two elements), first dim has 2 elements and then 2nd one has 4 elements.
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr) 
print(arr.shape) # Returns (1,1,1,1,4). Which means the array has 5 dimensions, first dim has 1 element and then 2nd one has 1 element and so on. Last one has 4 elements.
# %% Array reshaping
import numpy as np
# Reshape from 1D to 2D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3) # New array has 4 rows and 3 columns
print(newarr)
# Reshape from 1D to 3D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2) # New array has 2 2D arrays, each with 3 rows and 2 columns
print(newarr)
# Copy or View?
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr.reshape(3,2))
print(arr.reshape(3,2).base) # Returns the original array as it is a view.
# Unknown Dimensions
arr = np.array([1, 2, 3, 4, 5, 6,7,8])
newarr = arr.reshape(2, 2, -1) # -1 means unknown dimension. NumPy automatically fills it for you. You're only allowed to have one unknown at a time.
print(newarr)
print(newarr.shape) # Returns (2,2,3)
# Flattening
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1) # Flattens the array
print(newarr)
print(newarr.shape) # Returns (6,)
# %% Iterating through an array
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
for x in arr:
    print(x) # Iterates through each element one by one
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    print(x) # Prints each 1-D array.
# To print each element, use nested for loop
for x in arr:
    for y in x:
        print(y)
# Similarly, to print the scalars in a 3-D array:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)
# Using nditer
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x) # Prints each element one by one
# Iterating arrays with different data types
arr=np.array([1,2,3,4])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']): # op_dtypes changes the data type of the output. flags=['buffered'] is used to make a temporary space to make it work.
    print(x) # Returns each element as a byte string
# Iterating arrays with different steps
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
  print(x) # Returns every second element in the array
# Iterating through enumeration - Loops through all elements and tells where each one is.
arr = np.array([1, 2, 3, 4])
for idx, x in np.ndenumerate(arr):
  print(idx, x) # Returns index and value of each element

arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
for idx, x in np.ndenumerate(arr1):
    print(idx, x)
# %% Joining NumPy arrays
import numpy as np

# Using concatenate
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2))
print(arr)
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

# Using stack
arr1 = np.array([[1, 2],[3, 4]])
arr2 = np.array([[5, 6],[7, 8]])
arr = np.stack((arr1, arr2)) # Default axis = 0
print(arr)
arr = np.stack((arr1, arr2), axis=1)
print(arr)
arr = np.stack((arr1, arr2), axis=2)
print(arr)
# Using hstack,vstack,dstack
arr = np.hstack((arr1, arr2))
print(arr)
arr = np.vstack((arr1, arr2)) # Does the same thing as stack with axis 1
print(arr)
arr = np.dstack((arr1, arr2)) # Does the same thing as stack with axis 2
print(arr)
# %% Splitting arrays
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3) # Splits 1D array into 3 1D arrays
print(newarr)
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
newarr = np.array_split(arr, 3) # Splits 2D array into 3 2D arrays
print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3) # Splits across columns
print(newarr)
newarr = np.vsplit(arr, 3) # Splits across rows
print(newarr)
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
newarr = np.dsplit(arr, 3) # Splits across depth. Only for arrays with dim>=3
print(newarr)
# %% Searching an array
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x) # Returns the indices of the elements that are equal to 4
# Search Sorted method - Performs a binary search on the array and returns the index where the element should be inserted to maintain the order of the array
arr = np.array([1, 2, 3, 4, 5, 6])
x = np.searchsorted(arr, 7)
print(x)
# We assume the array is sorted while applying this method
# Usually the method returns the index from the left, but we can also make it return from the right
arr = np.array([1, 2, 3, 4, 5, 6])
x = np.searchsorted(arr, 7, side='right')
print(x)
# Searching for multiple values
arr=np.array([1,2,3,4,5,6])
x=np.searchsorted(arr,[2,4,6])
print(x) # Returns the indices of the elements that are equal to 2, 4, and 6. Output is an array.
# %% Sorting an array
import numpy as np
arr = np.array([3, 2, 0, 1, 5])
print(np.sort(arr)) # Returns a sorted array

# Can sort arrays of strings as well
arr = np.array(['banana', 'apple', 'cherry'])
print(np.sort(arr)) # Returns elements sorted in alphabetical order

# Sorting a multidimensional array
arr = np.array([[3, 2, 4], [1, 0, 5]])
print(np.sort(arr)) # Sorts both arrays
# %% Filter Arrays
import numpy as np

# Create an array from the elements on index 0 and 2
arr = np.array([1, 2, 3, 4, 5, 6])
filter_arr = [True, False, True, False, True, False]
newarr = arr[filter_arr]
print(newarr)

# Create a filter array where the values are higher than 2
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = []
for element in arr:
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

# Creating filter array using existing array
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr > 2
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)