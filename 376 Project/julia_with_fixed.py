import numpy as np
import matplotlib.pyplot as plt

# Define parameters
width, height = 1000, 1000
x_min, x_max = -2, 2
y_min, y_max = -2, 2
max_iter = 256

# Function to generate Julia set for a given c
def julia_set(c, width, height, x_min, x_max, y_min, y_max, max_iter):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    
    # Initialize the output array for the number of iterations
    iterations = np.zeros(Z.shape, dtype=int)
    mask = np.ones(Z.shape, dtype=bool)
    
    # Iterate the quadratic map z = z^2 + c
    for i in range(max_iter):
        Z[mask] = Z[mask]**2 + c
        mask = mask & (np.abs(Z) < 2)
        iterations[mask] = i
    
    return iterations

# Function to calculate fixed points of z^2 + c in period 1
def fixed_points(c):
    # Solve z^2 + c = z => z^2 - z + c = 0
    discriminant = 1 - 4 * c
    sqrt_discriminant = np.sqrt(discriminant)
    fixed1 = (1 + sqrt_discriminant) / 2
    fixed2 = (1 - sqrt_discriminant) / 2
    return fixed1, fixed2

# Function to visualize fixed points and stability regions
def plot_julia_with_fixed_points(c, width, height, x_min, x_max, y_min, y_max, max_iter):
    julia = julia_set(c, width, height, x_min, x_max, y_min, y_max, max_iter)
    fixed1, fixed2 = fixed_points(c)
    
    # Generate grid for complex plane
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    
    # Compute stability of fixed points
    stability1 = abs(2 * fixed1)
    stability2 = abs(2 * fixed2)
    
    # Plot the Julia set
    plt.figure(figsize=(8, 8))
    plt.imshow(np.fliplr(julia), extent=[x_min, x_max, y_min, y_max], cmap='inferno')
    plt.colorbar(label="Number of iterations")
    
    # Overlay fixed points
    plt.scatter([fixed1.real], [fixed1.imag], color='white', label=f'Fixed Point 1 |2z|={stability1:.2f}')
    plt.scatter([fixed2.real], [fixed2.imag], color='cyan', label=f'Fixed Point 2 |2z|={stability2:.2f}')
    
    # Annotate stability of fixed points
    plt.annotate(f'|2z|={stability1:.2f}', (fixed1.real, fixed1.imag), color='white', fontsize=12)
    plt.annotate(f'|2z|={stability2:.2f}', (fixed2.real, fixed2.imag), color='cyan', fontsize=12)
    
    plt.title(f"Julia Set with Fixed Points for c = {c.real} + {c.imag}i")
    plt.xlabel("Re(z)")
    plt.ylabel("Im(z)")
    plt.legend(loc="upper right")
    
    plt.show()

# Visualize
c = complex(0.5,-0.25)
plot_julia_with_fixed_points(c, width, height, x_min, x_max, y_min, y_max, max_iter)