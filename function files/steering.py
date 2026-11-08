import numpy as np
from parameters import K,N,D
def calculate_weights(steer_deg):
    n=np.arange(N)
    steer=np.deg2rad(steer_deg)
    weights = np.exp(
        -1j * K * n * D * np.sin(steer)
    )
    return weights 