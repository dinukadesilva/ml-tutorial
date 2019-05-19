import numpy as np
import matplotlib.pyplot as plt

Y = np.array([3, 5, 7, 9, 11, 13, 15, 17, ])
X = np.array([1, 2, 3, 4, 5, 6, 7, 8])

n = 8

train_x = X
train_y = Y

a0 = 0
a1 = 0

alpha = 0.03
epoches = 100.0


plt.figure(figsize=(5, 5))


epoch = 0
while (epoch < epoches):
    print("[%d] #############################################" % epoch)
    print("a0      : ", a0)
    print("a1      : ", a1)
    y = a0 + (a1 * train_x)
    error = y - train_y
    mse = np.sum(error**2)
    print("mse   : ",mse)
    plt.scatter(X, y, color=str(epoch/ epoches))
    
    
    a0 = a0 - (alpha * (2/n) * np.sum(error))
    a1 = a1 - (alpha * (2/n) * np.sum(error * train_x ))
    epoch = epoch + 1

plt.scatter(X, Y, color='red', label='GT')
plt.legend()
plt.show()




