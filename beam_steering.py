
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ====================================
# 1. Project parameters
# ====================================
C = 3e8
FREQUENCY = 2.4e9
WAVELENGTH = C / FREQUENCY
K = 2 * np.pi / WAVELENGTH# wave no

N = 8 #no of array elements
D = WAVELENGTH / 2 #element spacing

STEERING_ANGLES = [-30, 0, 15, 30]
THETA_DEG = np.linspace(-90, 90, 3601)
THETA = np.deg2rad(THETA_DEG)

RESULTS = Path("results")
RESULTS.mkdir(exist_ok=True)

print(f"Wavelength = {WAVELENGTH:.4f} m")
print(f"Spacing = {D:.4f} m")
print(f"Number of elements = {N}")


# ====================================
# 2. Calculate the array factor
# ====================================
def calculate_pattern(steer_deg, spacing=D, n_elements=N):
    n = np.arange(n_elements)
    steer = np.deg2rad(steer_deg)

    # Phase weights for the desired direction
    weights = np.exp(
        -1j * K * n * spacing * np.sin(steer)
    )

    # Contribution of every element at every angle for 3601 angles for 8 elements
    phase = (
        K * spacing
        * np.sin(THETA[:, None])
        * n[None, :]
    )

    af = np.sum(   # calculation array factor 
        np.exp(1j * phase) * weights[None, :],
        axis=1
    )

    magnitude = np.abs(af) # calculation absolute value(magnitude) of array factor as it is complex
    normalized = magnitude / n_elements # doing normalisation 

    pattern_db = 20 * np.log10( #converting into decibels

        np.maximum(normalized, 1e-6)
    ) 

    return pattern_db # this return patterns


# ====================================
# 3. Plot beam steering patterns
# ====================================
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

plt.savefig(
    RESULTS / "steering_patterns.png",
    dpi=200
)
plt.show()


# ====================================
# 4. Measure peak direction
# ====================================
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


# ====================================
# 5. Estimate 3 dB beamwidth
# ====================================
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


pattern = calculate_pattern(-30)

print(
    "\nBroadside 3 dB beamwidth:",
    f"{beamwidth_3db(pattern):.2f} degrees"
)
