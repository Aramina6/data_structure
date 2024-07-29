# array_notes.py

# Python Lists (Arrays)

# 1. Creating a List (Array)
arr = [1, 2, 3, 4, 5]  # Creating a list with elements 1, 2, 3, 4, 5

# 2. Accessing Elements
print(arr[0])  # Output: 1 (Access the first element)
print(arr[-1]) # Output: 5 (Access the last element)

# 3. Modifying Elements
arr[1] = 10  # Change the second element to 10
print(arr)   # Output: [1, 10, 3, 4, 5]

# 4. Appending Elements
arr.append(6)  # Add 6 to the end of the list
print(arr)     # Output: [1, 10, 3, 4, 5, 6]

# 5. Inserting Elements
arr.insert(2, 7)  # Insert 7 at index 2
print(arr)        # Output: [1, 10, 7, 3, 4, 5, 6]

# 6. Removing Elements
arr.remove(10)  # Remove the first occurrence of 10
print(arr)      # Output: [1, 7, 3, 4, 5, 6]

# 7. Popping Elements
arr.pop()       # Remove the last element
print(arr)      # Output: [1, 7, 3, 4, 5]
arr.pop(1)      # Remove the element at index 1
print(arr)      # Output: [1, 3, 4, 5]

# 8. Slicing
print(arr[1:3]) # Output: [3, 4] (Elements from index 1 to 2)
print(arr[:2])  # Output: [1, 3] (Elements from the start to index 1)
print(arr[2:])  # Output: [4, 5] (Elements from index 2 to the end)

# 9. Finding Elements
index = arr.index(4)  # Find the index of the first occurrence of 4
print(index)          # Output: 2

# 10. Length of the List
length = len(arr)  # Get the number of elements in the list
print(length)      # Output: 4

# 11. Sorting
arr.sort()         # Sort the list in ascending order
print(arr)         # Output: [1, 3, 4, 5]
arr.sort(reverse=True)  # Sort the list in descending order
print(arr)         # Output: [5, 4, 3, 1]


# Using `array` Module

from array import array

# 1. Creating an Array
arr = array('i', [1, 2, 3, 4, 5])  # 'i' denotes integer type

# 2. Accessing and Modifying Elements
print(arr[0])  # Output: 1 (Access the first element)
arr[1] = 10    # Modify the second element
print(arr)     # Output: array('i', [1, 10, 3, 4, 5])

# 3. Appending and Extending Elements
arr.append(6)     # Append element 6
print(arr)        # Output: array('i', [1, 10, 3, 4, 5, 6])
arr.extend([7, 8])  # Extend array with multiple elements
print(arr)        # Output: array('i', [1, 10, 3, 4, 5, 6, 7, 8])

# 4. Inserting and Removing Elements
arr.insert(2, 7)  # Insert 7 at index 2
print(arr)        # Output: array('i', [1, 10, 7, 3, 4, 5, 6, 7, 8])
arr.remove(10)    # Remove the first occurrence of 10
print(arr)        # Output: array('i', [1, 7, 3, 4, 5, 6, 7, 8])

# 5. Popping Elements
arr.pop()         # Pop the last element
print(arr)        # Output: array('i', [1, 7, 3, 4, 5, 6, 7])
arr.pop(1)        # Pop the element at index 1
print(arr)        # Output: array('i', [1, 3, 4, 5, 6, 7])

# 6. Finding the Length of the Array
length = len(arr)  # Get the number of elements
print(length)      # Output: 6

# 7. Accessing Array Buffer Information
print(arr.buffer_info())  # Output: (address, number of elements)


# Using NumPy

import numpy as np

# 1. Creating a NumPy Array
arr = np.array([1, 2, 3, 4, 5])  # Create a NumPy array

# 2. Basic Operations
print(arr + 2)        # Output: [3 4 5 6 7] (Add 2 to each element)
print(arr * 2)        # Output: [2 4 6 8 10] (Multiply each element by 2)
print(np.mean(arr))   # Output: 3.0 (Calculate the mean)
print(np.sum(arr))    # Output: 15 (Sum all elements)

# 3. Slicing and Indexing
print(arr[1:4])  # Output: [2 3 4] (Elements from index 1 to 3)

# 4. Array Reshaping
arr = np.array([[1, 2], [3, 4], [5, 6]])
reshaped = arr.reshape(2, 3)  # Reshape to 2x3 array
print(reshaped)
# Output:
# [[1 2 3]
#  [4 5 6]]

# 5. Broadcasting
arr2 = np.array([1, 2, 3])
arr3 = arr2 + 1  # Add 1 to each element
print(arr3)      # Output: [2 3 4]

# 6. Array Operations with Scalars
print(arr2 * 2)  # Output: [2 4 6]

# 7. Aggregation Functions
print(np.max(arr2))  # Output: 3 (Find maximum element)
print(np.min(arr2))  # Output: 1 (Find minimum element)
