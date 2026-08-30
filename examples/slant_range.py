import numpy as np
from scripts.slant_range_circular import computeSlantRange

# Observer position in ECI (km) - e.g., a ground station
R_obs = np.array([4500.0, 5500.0, 3500.0]) 

altitude = 420.0 # km

# The telescope measures the satellite's direction against the stars.
# Let's invent an observation: RA = 45°, Dec = 30°
RA_deg = 45.0
Dec_deg = 30.0

computeSlantRange(R_obs, altitude, RA_deg, Dec_deg)
