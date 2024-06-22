import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
import random

# Defining the function and integration boundary
def f(x):
    return x ** 2

a = 0 # Lower bound
b = 2 # Upper bound

# Creating a range of values for x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Creating a graph
fig, ax = plt.subplots()

# Drawing a function
ax.plot(x, y, 'r', linewidth=2)

# Filling the area under the curve
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Setting up the graph
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Adding integration limits and graph title
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Graph of integration of f(x) = x^2 from ' + str(a) + ' to ' + str(b))
plt.grid()
plt.show()

# Define the integration boundaries, for example, from 0 to 1
a = 0 # lower bound
b = 2 # upper bound

# Calculating the integral
result, error = spi.quad(f, a, b)

print("Integral: ", result)

xmax = b
ymax = f(xmax)

def is_inside(x, y):
    """Checks if the point (x, y) is inside the triangle."""
    return y <= f(x)

def monte_carlo_simulation(a, b, num_experiments):
    """Performs a series of Monte Carlo simulations."""
    average_area = 0

    for _ in range(num_experiments):
        # Generate random points
        points = [(random.uniform(0, xmax), random.uniform(0, ymax)) for _ in range(15000)]
        # Selecting points that are inside the triangle
        inside_points = [point for point in points if is_inside(point[0], point[1])]

        # Calculating the area by the Monte Carlo method
        M = len(inside_points)
        N = len(points)
        area = (M / N) * (xmax * ymax)

        # Adding to the average area
        average_area += area

    # Calculating the average area
    average_area /= num_experiments
    return average_area


# Number of experiments
num_experiments = 100

# Execution of the simulation
average_area = monte_carlo_simulation(a, b, num_experiments)
print(f"Average area of the triangle for {num_experiments} experiments: {average_area}")
