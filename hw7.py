import numpy as np

arr1 = np.array(range(1, 10))
arr2 = arr1.reshape(3, 3)
arr3 = np.linspace(0, 10, 5, dtype=float)
arrOnes = np.ones((3, 4), dtype=int)
arrZeros = np.zeros((3, 4), dtype=int)
arrUnit = np.identity(3, dtype=int)
martrix1 = np.array([[1, 3, 3], [6, 5, 6], [9, 9, 9]], dtype=int)
martrix2 = np.linalg.inv(martrix1)
maxOfMatrix1 = martrix1.max()
ColumnMax = martrix1.max(axis=0)
LineMean = martrix1.mean(axis=1)
variance = martrix1.var(axis=0)
martrix3 = martrix1[[0, 1]]
martrix4 = martrix1[[0, 1]][:, [1, 2]]
maxList = martrix1[martrix1 > 3]
print(maxList)
