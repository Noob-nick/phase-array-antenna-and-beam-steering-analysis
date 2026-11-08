import numpy as np

C = 3e8
FREQUENCY = 2.4e9
WAVELENGTH = C / FREQUENCY
K = 2 * np.pi / WAVELENGTH# wave no

N = 8 #no of array elements
D = WAVELENGTH / 2 #element spacing

STEERING_ANGLES = [-30, 0, 15, 30]
THETA_DEG = np.linspace(-90, 90, 3601)
THETA = np.deg2rad(THETA_DEG)
