import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import zoom

# import random_walk
# rw = random_walk.Randomwalk()

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(15,9))

def map_walk(grid, start, num_steps):
    x, y = start
    for num in range(num_steps):
        dx, dy = np.random.choice([-1,0,1]), np.random.choice([-1,0,1])
        x = max(0, min(grid.shape[0] - 1, x + dx))
        y = max(0, min(grid.shape[0] - 1, y + dy))
        grid[x,y] += 1

map_size = 100
map_grid = np.zeros((map_size, map_size))

num_walks = 10
walk_steps = 10000

for num in range(num_walks):
    start_point = (np.random.randint(map_size), np.random.randint(map_size))
    map_walk(map_grid, start_point, walk_steps)

smooth_map = zoom(map_grid, 10, order=3)

plt.imshow(smooth_map,cmap='terrain',origin='lower')
plt.colorbar(label='Elevation')
plt.title("Map")
plt.show()