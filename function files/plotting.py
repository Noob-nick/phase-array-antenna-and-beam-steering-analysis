import matplotlib.pyplot as plt
from parameters import THETA_DEG,STEERING_ANGLES
from radiation_pattern import calculate_pattern

def plot_pattern(pattern_db, steer_deg):
   plt.figure(figsize=(10, 6)) #this creates a figure

   for steer_deg in STEERING_ANGLES:
    pattern = calculate_pattern(steer_deg) # applied for loop calculates pattern for each angle

    plt.plot(
        THETA_DEG,# x axis is angle
        pattern,# y axis is normalised array factor
        label=f"Steering angle = {steer_deg} deg"
    )

    plt.xlabel("Observation angle (degrees)")
    plt.ylabel("Normalized array factor (dB)")
    plt.title("Phased-Array Beam Steering")
    plt.xlim(-90, 90)
    plt.ylim(-60, 2)
    plt.grid(True)
    plt.legend() 
    plt.tight_layout()

   
    plt.show()

  