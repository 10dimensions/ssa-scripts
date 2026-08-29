# Constants
mu = 398600.4418      # km^3/s^2
R_E = 6378.137        # km
J2 = 1.08263e-3       # dimensionless

# Normal conditions vs. Geomagnetic Storm conditions
# During a storm, the thermosphere heats up, expanding outward. 
# This increases BOTH the base density and the scale height.
DENSITY_NORMAL_200KM = 3.0e-10   # kg/m^3 (Quiet sun)
DENSITY_STORM_200KM  = 1.5e-9    # kg/m^3 (5x increase, matching Feb 2022 event)

SCALE_HEIGHT_NORMAL = 35000      # meters (Quiet)
SCALE_HEIGHT_STORM  = 55000      # meters (Expanded due to heating)
