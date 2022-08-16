import numpy as np
import matplotlib.pyplot as plt
plt.show()

#configuration
D = 2
k = 3
N = 300

      #create the data
mu1 = np.array([0, 0])
mu2 = np.array([5, 5])
mu3 = np.array([0, 5])

X = np.zeros((N, D))
X[:100, :] = np.random.randn(100, D) + mu1
X[100:200, :] = np.random.randn(100, D) + mu2
X[200:, :] = np.random.randn(100,  D) + mu3

Y = np.array([0] * 100 + [1] * 100 + [2] * 100)

# visualize the data
plt.scatter(X[:,0],X[:,1], c=Y);
plt.show()

#How to get back a D-sized vector when taking the mean?
X.mean(axis=0).shape


#find the mean of each cluster
means = np.zeros((k,D))
means[0,:] = X[Y == 0].mean(axis=0)
means[1,:] = X[Y == 1].mean(axis=0)
means[2,:] = X[Y == 2].mean(axis=0)

#plot the mean with the data
plt.scatter(X[:,0],X[:,1], c=Y); #same as before
plt.show()
plt.scatter(means[:,0],means[:,1], s=500,c = 'red',marker='*');
plt.show()




