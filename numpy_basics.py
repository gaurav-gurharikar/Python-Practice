import numpy as np

print(np.__version__)

#Create array
array = np.array([1,2,3,4])
print(array)

array = array*2
print(array)

#No. of dimensions
print(array.ndim)

#Slicing
array = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,16]])
#array[start:end:step]
print(array[0:4:2])

print(array[:, 2])

#Arithmetic
array = np.array([1,2,3,4])
print(array + 1)
print(array - 2)
print(array * 3)
print(array / 4)
print(array ** 5)

print(array == 3) #Returns boolean array
print(array > 2)

array1 = np.array([1,2,3,4])
array2 = np.array([5,6,7,8])
print(array1 + array2)

#Broadcasting
array1 = np.array([[1,2,3,4]])
array2 = np.array([[1],[2],[3],[4]])
print(array1.shape)
print(array2.shape)
print(array1 * array2)

#Aggregate functions
array = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(np.sum(array))
print(np.mean(array))
print(np.min(array))
print(np.max(array))
print(np.argmin(array)) #Position of min
print(np.argmax(array)) #Position of max

print(np.sum(array, axis=0)) #Sum of column elements
print(np.sum(array, axis=1)) #Sum of row elements

#Filtering
ages = np.array([[21,18,9,25], [12,36,7,19]])
adults = ages[ages>=18]
print(adults)

adults = np.where(ages>=18, ages, 0) #where(condition, value_when_true, value_when_false)
print(adults)

#Random numbers
rng = np.random.default_rng()
print(rng.integers(low=1, high=11, size=(2,2)))

print(np.random.uniform(0,2))

array = np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)