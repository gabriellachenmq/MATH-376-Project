import numpy as np

def load_complex_csv(file_path):
    with open(file_path, 'r') as f:
        data = [line.strip().replace('i', 'j') for line in f]
    return np.array([complex(num) for num in data])

# Compute stability for periodic points
def compute_stability(points, period, c):
    stabilities = []
    for z0 in points:
        # Compute derivative recursively
        z = z0
        derivative = 1  # Start with identity derivative
        for _ in range(period):
            derivative *= 2 * z  # Multiply by f'(z) = 2z
            z = z**2 + c  # Iterate the map
        stability = np.abs(derivative)
        stabilities.append((z0, stability))
    return stabilities

# Example usage
periodic_points = {
    1: load_complex_csv('periodic_points_period_1.csv'),
    2: load_complex_csv('periodic_points_period_2.csv'),
    3: load_complex_csv('periodic_points_period_3.csv'),
    4: load_complex_csv('periodic_points_period_4.csv'),
    5: load_complex_csv('periodic_points_period_5.csv')
}

c = -0.7 + 0.3j 

# Analyze stability for each period
for period, points in periodic_points.items():
    stabilities = compute_stability(points, period, c)
    print(f"Period-{period} Stabilities:")
    for point, stability in stabilities:
        classification = "Stable" if stability < 1 else "Neutral" if stability == 1 else "Unstable"
        print(f"  Point: {point}, |λ| = {stability:.4f}, {classification}")
