import numpy as np
import matplotlib.pyplot as plt

def zoomed_julia_set(c, x_min, x_max, y_min, y_max, zoom_width, zoom_height, max_iter):

    # High-resolution grid
    x = np.linspace(x_min, x_max, zoom_width)
    y = np.linspace(y_min, y_max, zoom_height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    # Initialize the iteration array
    iterations = np.zeros(Z.shape, dtype=int)
    mask = np.ones(Z.shape, dtype=bool)

    # Iterate the map
    for i in range(max_iter):
        Z[mask] = Z[mask]**2 + c
        mask = mask & (np.abs(Z) < 2)
        iterations[mask] = i

    return iterations

# Function to plot the zoomed Julia set
def plot_zoomed_julia(c, x_min, x_max, y_min, y_max, zoom_width, zoom_height, max_iter):
    zoomed_julia = zoomed_julia_set(c, x_min, x_max, y_min, y_max, zoom_width, zoom_height, max_iter)
    
    plt.figure(figsize=(8, 8))
    plt.imshow(np.fliplr(zoomed_julia), extent=[x_min, x_max, y_min, y_max], cmap='inferno')
    plt.colorbar(label="Number of iterations")
    plt.title(f"Zoomed Julia Set for c = {c.real} + {c.imag}i")
    plt.xlabel("Re(z)")
    plt.ylabel("Im(z)")
    plt.show()

c = complex(-0.8,0.156)  
x_min, x_max = -0.07, 0 
y_min, y_max = -0.5, -0.48
zoom_width, zoom_height = 2000, 2000  # Increased resolution
max_iter = 512  # High iteration

# Plot the zoomed Julia set
plot_zoomed_julia(c, x_min, x_max, y_min, y_max, zoom_width, zoom_height, max_iter)
