import numpy as np
import matplotlib.pyplot as plt

def zoomed_julia_set(c, x_min, x_max, y_min, y_max, zoom_width, zoom_height, max_iter):
    """
    Generate a high-resolution Julia set for a zoomed-in region.

    Args:
        c: Complex parameter for the Julia set.
        x_min, x_max, y_min, y_max: The bounds of the zoomed region.
        zoom_width: Number of points in the x direction (increased resolution).
        zoom_height: Number of points in the y direction (increased resolution).
        max_iter: Maximum number of iterations for divergence testing.

    Returns:
        A high-resolution Julia set image for the zoomed-in region.
    """
    # Create a high-resolution grid
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

# Example: Zooming into a small region of the Julia set
c = complex(-0.8,0.156)  # The same parameter as before
x_min, x_max = -0.07, 0  # Zoomed region bounds
y_min, y_max = -0.5, -0.48    # Zoomed region bounds
zoom_width, zoom_height = 2000, 2000  # Increased resolution
max_iter = 512  # High iteration count for detail

# Plot the zoomed Julia set
plot_zoomed_julia(c, x_min, x_max, y_min, y_max, zoom_width, zoom_height, max_iter)
