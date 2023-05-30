# imports
import numpy as np
import random
import matplotlib.pyplot as plt

# diamond square algorithm
def diamond_square(n, roughness):
    size = 2**n + 1
    terrain = np.zeros((size, size))

    # Set corner points
    terrain[0, 0] = random.uniform(-1, 1)
    terrain[0, -1] = random.uniform(-1, 1)
    terrain[-1, 0] = random.uniform(-1, 1)
    terrain[-1, -1] = random.uniform(-1, 1)

    step = size - 1

    while step > 1:
        half = step // 2
        scale = roughness / size

        # Diamond step
        for y in range(half, size - 1, step):
            for x in range(half, size - 1, step):
                avg = terrain[y - half, x - half] + terrain[y - half, x + half] + terrain[y + half, x - half] + terrain[y + half, x + half]
                terrain[y, x] = avg / 4 #+ random.uniform(-scale, scale)

        # Square step
        for y in range(0, size, step):
            for x in range((y + half) % step, size, step):
                avg = terrain[(y - half) % size, x] + terrain[(y + half) % size, x] + terrain[y, (x + half) % size] + terrain[y, (x - half) % size]
                terrain[y, x] = avg / 4 #+ random.uniform(-scale, scale)

        step //= 2
        roughness /= 2

    return terrain

# parameters
n = 10  # Number of iterations (controls the size of the terrain, 2^n + 1)
roughness = 0.000001  # Roughness parameter

# generate terrain
terrain = diamond_square(n, roughness)

# # generate figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.arange(0, terrain.shape[0])
y = np.arange(0, terrain.shape[1])
X, Y = np.meshgrid(x, y)
Z = terrain[X, Y]

# plot the terrain
ax.plot_surface(X, Y, Z, cmap='terrain')

# show the terrain
plt.show()
