import numpy as np
import matplotlib.pyplot as plt
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

# Note - there is no stochasticity in here! It's all deterministic

default_s = 10 # sigma
default_r = 28 # rho
default_b = 2.667 # beta

def lorenz_deriv(x, y, z, s=default_s, r=default_r, b=default_b):
    '''
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    '''
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

def lorenz_generator(
        initial_values,
        s=default_s, r=default_r, b=default_b,
        dt=0.01, num_steps=10000
    ):
    values = np.empty((3, num_steps + 1))
    values[:, 0] = np.array(initial_values)
    # Step through "time", calculating the partial derivatives at the current point
    # and using them to estimate the next point
    for i in range(num_steps):
        x_dot, y_dot, z_dot = lorenz_deriv(
            values[0, i],
            values[1, i],
            values[2, i],
            s, r, b
        )
        values[0, i + 1] = values[0, i] + (x_dot * dt)
        values[1, i + 1] = values[1, i] + (y_dot * dt)
        values[2, i + 1] = values[2, i] + (z_dot * dt)
    return values

initial_values = (0., 1., 1.05)
lorenz_data = lorenz_generator(initial_values)


# Plot
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(*lorenz_data, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

plt.savefig("test.png")
plt.show()
