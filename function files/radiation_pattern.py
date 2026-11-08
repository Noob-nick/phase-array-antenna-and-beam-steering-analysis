import numpy as np
from parameters import K,N,D,THETA
from steering import calculate_weights

def calculate_pattern(steer_deg):
     n=np.arange(N)
     weights=calculate_weights(steer_deg)
     phase = (
        K * D
        * np.sin(THETA[:, None])
        * n[None, :]
    )
     af = np.sum(   # calculation array factor 
        np.exp(1j * phase) * weights[None, :],
        axis=1
    )

     magnitude = np.abs(af) # calculation absolute value(magnitude) of array factor as it is complex
     normalized = magnitude / N # doing normalisation 

     pattern_db = 20 * np.log10( #converting into decibels

        np.maximum(normalized, 1e-6)
    ) 
     return pattern_db # this return patterns
