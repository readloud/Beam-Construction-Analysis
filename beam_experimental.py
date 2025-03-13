import numpy as np
import matplotlib.pyplot as plt

# Beam parameters
L = 10  # Length of the beam (m)
P = 1000  # Point load (N)
x = np.linspace(0, L, 1000)  # Points along the beam

# Calculate reactions
R_A = P / 2
R_B = P / 2

# Initialize shear force and bending moment arrays
V = np.zeros_like(x)
M = np.zeros_like(x)

# Calculate shear force and bending moment
for i, xi in enumerate(x):
    if xi < L / 2:
        V[i] = R_A
        M[i] = R_A * xi
    else:
        V[i] = R_A - P
        M[i] = R_A * xi - P * (xi - L / 2)

# Plotting
plt.figure(figsize=(12, 6))

# Shear Force Diagram
plt.subplot(2, 1, 1)
plt.plot(x, V, label='Shear Force (V)')
plt.title('Shear Force Diagram')
plt.xlabel('Position along the beam (m)')
plt.ylabel('Shear Force (N)')
plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

# Bending Moment Diagram
plt.subplot(2, 1, 2)
plt.plot(x, M, label='Bending Moment (M)', color='orange')
plt.title('Bending Moment Diagram')
plt.xlabel('Position along the beam (m)')
plt.ylabel('Bending Moment (Nm)')
plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
