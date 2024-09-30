import numpy as np

# 1. create an array of 10 zeros, 10 ones, and 10 fives.


z= np.zeros((2,5))
print(z)

o= np.ones((2,5))
print(o)

ful= np.full((2,5),5)
print(ful)


# 2. create an array of integers from 30 to 70.

a= np.arange(30,71)
print(a)


# 3. create a 3x3 identity matrix.

a= np.array([[1,2,3],[4,5,6],[7,8,9]])

b= np.eye(3)
print(b)

# 4. Write a NumPy program to multiply two given arrays of the same size element-by-element.


a= np.array([[1,2],[4,5]])
b= np.array([[8,6],[9,3]])
result= np.dot(a,b)
print(result)


# 5. Write a NumPy program to swap rows and columns of a given array in reverse order.


a= np.array([[1,2,3],[4,5,6]])
print(a[::-1,::-1])



# 6. Write a NumPy program to calculate mean across dimension, in a 2D numpy array.


a= np.array([[3,5,8,7],[6,8,9,2]])
print(a.mean())


# 7. Write a NumPy program to calculate round, floor, ceiling, truncated and round (to the given number of decimals) of the input, element-wise of a given array.
#Sample output:
#Original array:
#[ 3.1 3.5 4.5 2.9 -3.1 -3.5 -5.9]
#around: [ 3. 4. 4. 3. -3. -4. -6.]
#floor: [ 3. 3. 4. 2. -4. -4. -6.]
#ceil: [ 4. 4. 5. 3. -3. -3. -5.]
#trunc: [ 3. 3. 4. 2. -3. -3. -5.]
#round: [3.0, 4.0, 4.0, 3.0, -3.0, -4.0, -6.0]


a= np.array([ 3.1,3.6,4.5,2.9,-3.1,-3.5,-5.9])
print(np.around(a))
print(np.floor(a))
print(np.ceil(a))
print(np.trunc(a))
print(np.round(a))


# 8. Write a NumPy program to compute the determinant of a given square array.


a= np.array([[8,4,6],[10,5,13],[8,2,9]])
print(a)
print(np.linalg.det(a))


# 9. find the maximum and minimum value of a given flattened array.


a= np.array([[8,3,5,6],[6,7,9,5]])
print(a.min(axis=0))
print(a.max(axis=0))
print(a.min(axis=1))
print(a.max(axis=1))


# 10. creates a 3D NumPy array and uses fancy indexing to select elements from specific rows and columns.


a= np.array([[[5,8,3],[9,6,2],[7,1,4]]])

index= [0]
print(a[0,0,index])
print(a[0,2,index])
print(a[0,1,index])


# 11. Write a NumPy program that performs element-wise addition using broadcasting.


a= np.array([[1,2,3],[4,5,6],[5,6,7]])
b= np.array([[6],[7],[4]])
print(a+b)
print(a.shape)
print(b.shape)


# 12. creates a 2D array x of shape (3, 4) and a 1D array y of shape (4,). Subtract y from each row of x using broadcasting.


x= np.array([[1,2,3,4],[5,6,4,7],[9,10,11,12]])
y = np.array([6,7,2,4])
print(x-y)


# 13. Replace all negative values in an array with 0.


a= np.array([-1,2,-3,4,-5,6,7,-8])
a[a<0]=0
print(a)    


# 14. Count the number of elements in an array that are greater than the mean.


a= np.array([5,6,7,8])
print(a.mean())
print(a>np.mean(a))
print(np.sum(a>np.mean(a)))
print(a[a>np.mean(a)])


# 15. Create a 1D array and remove all duplicate values.


a= np.array([5,6,4,4,8,8,8,6])
print(np.unique(a))
