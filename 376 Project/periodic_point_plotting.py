import numpy as np
import matplotlib.pyplot as plt

# Load periodic points
def load_complex_csv(file_path):
    with open(file_path, 'r') as f:
        data = [line.strip().replace('i', 'j') for line in f]
    return np.array([complex(num) for num in data])

# Load periodic points for each period
periodic_points = {
    1: load_complex_csv('periodic_points_period_1.csv'),
    2: load_complex_csv('periodic_points_period_2.csv'),
    3: load_complex_csv('periodic_points_period_3.csv'),
    4: load_complex_csv('periodic_points_period_4.csv'),
    5: load_complex_csv('periodic_points_period_5.csv'),
    6: load_complex_csv('periodic_points_period_6.csv')
}

# Julia set parameters
c = -0.7 + 0.3j
resolution = 1000
x = np.linspace(-2, 2, resolution)
y = np.linspace(-2, 2, resolution)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y
max_iter = 100
julia_set = np.full(Z.shape, True, dtype=bool)

# Generate Julia set
for i in range(max_iter):
    Z[np.abs(Z) > 1e5] = np.nan
    Z = Z**2 + c
    julia_set[np.abs(Z) > 2] = False

# Plot Julia set
plt.figure(figsize=(8, 8))
plt.imshow(np.fliplr(julia_set), extent=(-2, 2, -2, 2), cmap="binary")

# Colors for each period
colors = {
    1: 'fuchsia',
    2: 'turquoise',
    3: 'red',
    4: 'lime',
    5: 'yellow',
    6: 'cyan'  
}

# Overlay periodic points
for period, points in periodic_points.items():
    plt.scatter(
        np.real(points),
        np.imag(points),
        color=colors[period],
        marker='o',
        label=f'Period-{period}',
        s=50
    )

plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.title('Julia Set with Periodic Points for c = -0.7 + 0.3i')
plt.legend()
plt.show()
