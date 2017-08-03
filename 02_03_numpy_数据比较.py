import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[1, 2], [3, 5]])
print a[0, :]
print (a[0, :] == b[0, :]).all()
# if a[0,:].all(b[0,:])
#     print 'a'