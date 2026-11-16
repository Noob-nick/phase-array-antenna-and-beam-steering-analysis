
import numpy as np
from pathlib import Path

# Physical constants
C = 3e8
FREQUENCY = 2.4e9

# Derived parameters
WAVELENGTH = C / FREQUENCY
K = 2 * np.pi / WAVELENGTH

# Array parameters
N = 8
D = WAVELENGTH / 2

# Steering angles
STEERING_ANGLES = [-30, 0, 15, 30]

# Observation angles
THETA_DEG = np.linspace(-90, 90, 3601)
THETA = np.deg2rad(THETA_DEG)

# Results directory
RESULTS = Path("results")
RESULTS.mkdir(exist_ok=True)

print(f"Wavelength = {WAVELENGTH:.4f} m")
print(f"Spacing = {D:.4f} m")
print(f"Number of elements = {N}")
