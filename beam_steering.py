import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
#project parameters
c=3e8 #speed of light
frequency=2.4e9 
wavelength=c/frequency 
k=2*np.pi/wavelength

n=8  # no of elements
d= wavelength/2 # element spacing
steering_angles= [-30,0,15,30]
theta_deg=np.linspace(-90,90,3601)
theta=np.deg2rad(theta_deg)

results=Path("results")
results.mkdir(exist_ok=True)

print(f"Wavelength = {wavelength:.4f} m")
print(f"Spacing={d:4f} m")
print(f"Number of elements ={n}")
 
