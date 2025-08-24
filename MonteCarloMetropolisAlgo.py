import math 
import numpy as np
import sympy as sp
from scipy import integrate as integ
from matplotlib import pyplot as plt
import random


#Monte Carlo simulation of  a 2D Ising model using Metropolis algorithm






#8.1
#IC
T = 2
size = 10
iteration = 100*(size**2)
M = np.zeros(shape=(size, size))

#M Values
for a in range(0,size):
  for b in range(0,size):
    M[a][b] = np.random.choice([-1, 1])
#Delta U func
def U(x,y):

  if x == 0:
    left = size-1
  else:
    left = x - 1
  if x == size-1:
    right = 0
  else:
    right = x + 1
  if y == 0:
    top = size-1
  else:
    top = y - 1
  if y == size-1:
    bottom = 0
  else:
    bottom = y + 1

  DU = M[x][y]*(M[left][y]+M[right][y]+M[x][top]+M[x][bottom])*(2)
  return DU
#Monte Carlo
for x in range(0,iteration):
  i = np.random.randint(0,size-1)
  j = np.random.randint(0,size-1)
  deltaU = U(i,j)
  if deltaU <= 0 or np.random.rand() < np.exp(-deltaU / T):
    M[i][j] *= -1

#Plot
plt.pcolormesh(M, edgecolors = 'k', cmap = 'gray')
plt.show()