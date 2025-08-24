# Monte Carlo simulation of the 2D Ising model at different temperatures
# Using Metropolis algorithm
import numpy as np
from matplotlib import pyplot as plt

# Parameters
size = 20  # Size of the grid
iteration = 100*(size**2)
temperatures = [4.0, 2.0, 1.0]  # Three different temperatures

# Initialize ONE grid that we'll use for all simulations
M_initial = np.random.choice([-1, 1], size=(size, size))

# Energy function
def U(M, x, y):
    neighbors = M[(x-1)%size, y] + M[(x+1)%size, y] + M[x, (y-1)%size] + M[x, (y+1)%size]
    return M[x, y] * neighbors * 2


# Create 1x4 subplot
fig, axes = plt.subplots(1, 4, figsize=(16, 4))

# Plot 1: Initial state
axes[0].pcolormesh(M_initial, edgecolors='k', cmap='gray')
axes[0].set_title('Initial Random State')

# Plots 2-4: Different temperatures
for idx, T in enumerate(temperatures):
    M = M_initial.copy()
    
    # Monte Carlo simulation
    for x in range(iteration):
        i = np.random.randint(0, size)
        j = np.random.randint(0, size)
        deltaU = U(M, i, j)
        if deltaU <= 0 or np.random.rand() < np.exp(-deltaU / T):
            M[i][j] *= -1
    
    axes[idx + 1].pcolormesh(M, edgecolors='k', cmap='gray')
    axes[idx + 1].set_title(f'T = {T}')

plt.tight_layout()
plt.show()