import numpy as np

arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr)


#Finding the size of each array element
#finding the size of each item in the array
import numpy as np
a = np.array([[1,2,3]]);
print("Each item contains",a.itemsize,"bytes")


#finding the data type of each array item
import numpy as np
a = np.array([[1,2,3]]);
print("Each item is of the type",a.dtype)


#finding the data type of each array item
import numpy as np
a = np.array([[1,'A',3]]);
print("Each item is of the type",a.dtype)


import numpy as np
a = np.array([[1,2,3,4,5,6,7]])
print("Array Size:",a.size)
print("Shape:",a.shape)


import numpy as np
a = np.array([[1,2,3,4],[8,5,6,7]])
print("Array Size:",a.size)
print("Shape:",a.shape)


import numpy as np
a = np.array([[1,2],[3,4],[5,6]])
print("printing the original array..")
print(a)
a=a.reshape(2,3)
print("printing the reshaped array..")
print(a)



import numpy as np
a = np.array([1,2,3,10,15,4])
print("The array:",a)
print("The maximum element:",a.max())
print("The minimum element:",a.min())
print("The sum of the elements:",a.sum())


import numpy as np
a = np.array([[1,2,30],[10,15,4]])
print(np.sqrt(a))
print(np.std(a))


#Arithmetic operations on the array
#The numpy module allows us to perform the arithmetic operations on multi-dimensional arrays directly.

import numpy as np
a = np.array([[1,2,30],[10,15,4]])
b = np.array([[1,2,3],[12, 19, 29]])
print("Sum of array a and b\n",a+b)
print("Product of array a and b\n",a*b)
print("Division of array a and b\n",a/b)



#Array Concatenation
#The numpy provides us with the vertical stacking and horizontal stacking which allows us to concatenate two multi-dimensional arrays vertically or horizontally.

import numpy as np
a = np.array([[1,2,30],[10,15,4]])
b = np.array([[1,2,3],[12, 19, 29]])
print("Arrays vertically concatenated\n",np.vstack((a,b)));
print("Arrays horizontally concatenated\n",np.hstack((a,b)))


#Numpy array from existing data

#creating numpy array using the list

import numpy as np
l=[1,2,3,4,5,6,7]
a = np.asarray(l);
print(type(a))
print(a)


#creating a numpy array using Tuple

import numpy as np
l=(1,2,3,4,5,6,7)
a = np.asarray(l);
print(type(a))
print(a)


#creating a numpy array using more than one list
import numpy as np
l=[1,2,3,4,5,6,7]
a = np.asarray(l);
print(type(a))
print(a)


#BROADCASTING
import numpy as np
a = np.array([[1,2,3,4],[2,4,5,6],[10,20,39,3]])
b = np.array([2,4,6,8])
print("\nprinting array a..")
print(a)
print("\nprinting array b..")
print(b)
print("\nAdding arrays a and b ..")
c = a + b;
print(c)


#NumPy String Functions
#numpy.char.add() method

import numpy as np
print("Concatenating two string arrays:")
print(np.char.add(['welcome','Hi'], [' to CYRSTAL', ' read python'] ))


#numpy.char.multiply() method
import numpy as np
print("Printing a string multiple times:")
print(np.char.multiply("hello ",3))


#numpy.char.center() method

import numpy as np
print("Padding the string through left and right with the fill char *");
#np.char.center(string, width, fillchar)
print(np.char.center("CRYSTAL", 20, '*'))


#numpy.char.capitalize() method
import numpy as np
print("Capitalizing the string using capitalize()...")
print(np.char.capitalize("welcome to crystal"))


#numpy.char.title() method
import numpy as np
print("Converting string into title cased version...")
print(np.char.title("welcome to crystal"))


#numpy.char.lower() method
import numpy as np
print("Converting all the characters of the string into lowercase...")
print(np.char.lower("WELCOME TO CRYSTAL"))


#numpy.char.upper() method
import numpy as np
print("Converting all the characters of the string into uppercase...")
print(np.char.upper("welcome to crystal"))
