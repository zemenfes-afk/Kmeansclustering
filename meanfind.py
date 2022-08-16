import numpy as np
import matplotlib.pyplot as plt
plt.show()

#configuration/intialization
D = 2
k = 3
N = 300
#create the data
means = np.array([[0, 0] ,[0, 5],[5, 5],])

X = np.zeros((N, D))
X[:100, :] = np.random.randn(100, D) + means[0]
X[100:200, :] = np.random.randn(100, D) + means[1]
X[200:, :] = np.random.randn(100,  D) + means[2]

Y=np.zeros(N)
for n in range (N):
    closest_K = -1
    min_dist = float('inf')
for k in range (k):
    d = (X[n] - means[k]).dot(X[n] - means[k])
    if d < min_dist:
        min_dist = d
        closest_K = k
        Y[n] = closest_K
#visualiza the data
plt.scatter(X[:,0], X[:,1], c=Y);
plt.show()
