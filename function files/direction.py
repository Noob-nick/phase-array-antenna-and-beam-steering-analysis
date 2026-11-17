import numpy as np

from parameters import STEERING_ANGLES, THETA_DEG
from radiation_pattern import calculate_pattern

def direction():
    print("\nBeam-direction validation")   # this is used to check if antenna is steering in desired direction or not

    for steer_deg in STEERING_ANGLES:
     pattern = calculate_pattern(steer_deg)

    peak_index = np.argmax(pattern) # this finds the  index of max value in pattern
    measured_angle = THETA_DEG[peak_index]# measured angle at that index 
    error = measured_angle - steer_deg # checked error between measured angle and steered angle for validation

    print(
        f"Requested: {steer_deg:>3} deg | "
        f"Measured: {measured_angle:>6.2f} deg | "
        f"Error: {error:>6.2f} deg"
    )
