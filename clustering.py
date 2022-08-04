

import random
from re import U

import numpy as np

#Variables - Clustering
N = 60   #edges = n*dl = m*dr = N
K = 4    #num of clusters ---> n = k 
#Variables - Bipartite Graph
dl =15   #degree left side
dr = 2   #degree right side
n = 4    #left side
m = 30   #right side


data = np.zeros((N, n+m))


right_deg = np.array([dr]*m) 
left_deg = np.array([dl]*n) 

print("Left Degree:", left_deg)
print("Right Degree:", right_deg)


for i in range(N): 
    

    x = np.random.choice(m, p=right_deg / np.sum(right_deg))
    
   # print("y, x+N: ", y,x+m)

    y = np.random.choice(n, p=left_deg / np.sum(left_deg))
    

    data[i][x+n] = 1
    data[i][y] = 1

    right_deg[x] -= 1
    left_deg[y] -= 1
    
    
""""   
row = np.array([N*d])
data = np.append(right_deg,[row],axis=0)

col = np.array([Nd*2*N+1])
data = np.append(left_deg,[col],axis=0)
"""

filename = "Dataset"
np.savetxt(filename + ".txt", data, fmt = '%u', delimiter=" ")

 
print("Dataset:", data)


