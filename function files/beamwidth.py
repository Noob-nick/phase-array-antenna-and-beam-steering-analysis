import numpy as np
from parameters import THETA_DEG
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

    beamwidth = THETA_DEG[right] - THETA_DEG[left]

    return beamwidth

