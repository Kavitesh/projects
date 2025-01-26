#
print("{two} => {one}".format(one=1,two=2))
print([a*2 for a in [1,2,3]]) 
print(["{two} => {one}".format(one=a,two=b) for a,b in [(1,11),(2,22)]])
print(list(map(lambda item: item*3,[1,2,3,4,5,6])))
print (list(filter(lambda item: item>3,[1,2,3,4,5,6])))

import numpy as np

print(np.array([1,2,3]))
print(np.arange(1,3,2))
print(np.zeros(2))
print(np.ones((2,2)))
print(np.eye(2))
print(np.linspace(1,5,9))
print(np.random.rand(2,3))
print(np.random.randint(1,30,(2,3)))
print(np.random.randn(10,3))
print(np.array([1,2,3,4]).reshape(2,2))
print(np.array([1,2,3,4]).min())
print(np.array([1,2,3,4,3,2]).argmax())
print(np.array([[1,2,3],[4,3,7],[2,7,6]]).shape)
print(np.array([[1,2,3],[4,3,7],[2,7,111111111111]]).dtype)

x = np.arange(0,10)
x[0:3]=10
print(x)

x = x.copy()#np.arange(0,10) 
slice=x[1:5]
slice[:] = 11
print(slice, x) 

x = np.array([[ 0.,  0.,  0. ], [ 1.,  1.,  1.],[ 2.,  2.,  2.],[ 3.,  3.,  3.]])
print(x[[1,3],[1]]) 

x = np.arange(1,7)
print(x>3)
print(x[x>3])