import matplotlib.pyplot as plt
import numpy as np
from parameters import THETA_DEG,STEERING_ANGLES,RESULTS
from radiation_pattern import calculate_pattern

def plot_pattern( ):
  
   for steer_deg in STEERING_ANGLES:
    plt.figure(figsize=(10, 6)) #this creates a figure
    
    pattern = calculate_pattern(steer_deg) # applied for loop calculates pattern for each angle
    def beamwidth_3db(pattern_db): # this function calculates beamwidth of pattern
           peak = np.argmax(pattern_db)# calculates index at which max peak occurs in pattern
           threshold = pattern_db[peak] - 3.0 # for calculating beamwidth 3db below its peak therefore 
        # subtracting 3db from max peak if peak =18db then will be calculating beamwidth for 15 db
    
           left = peak
           while left > 0 and pattern_db[left] >= threshold:
             left -= 1
    
           right = peak
           while (
            right < len(pattern_db) - 1
            and pattern_db[right] >= threshold
             ):
            right += 1
    
            return THETA_DEG[right] - THETA_DEG[left]
    
    
    print(
    "\nBroadside 3 dB beamwidth:",
    f"{beamwidth_3db(pattern):.2f} degrees"
     )

    
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
    
    plt.savefig(
            RESULTS / f"steering_{steer_deg}.png",
            dpi=200
        )
   
    plt.show()

  