# Constants
mu = 398600.4418      # km^3/s^2
mu_m = 3.986e14          # Earth's gravitational parameter (m^3/s^2)
R_E = 6378.137        # km
R_E_m = 6378000          # Earth's equatorial radius (m)
J2 = 1.08263e-3       # dimensionless

# Reference altitude for density (200 km)
H_REF = 200000         # meters

# Normal conditions vs. Geomagnetic Storm conditions
# During a storm, the thermosphere heats up, expanding outward. 
# This increases BOTH the base density and the scale height.
DENSITY_NORMAL_200KM = 3.0e-10   # kg/m^3 (Quiet sun)
DENSITY_STORM_200KM  = 1.5e-9    # kg/m^3 (5x increase, matching Feb 2022 event)

SCALE_HEIGHT_NORMAL = 35000      # meters (Quiet)
SCALE_HEIGHT_STORM  = 55000      # meters (Expanded due to heating)

# Satellite parameters (approximating a Starlink v1.5 satellite)
MASS = 260.0           # Mass (kg)
AREA = 15.0            # Cross-sectional area facing velocity vector (m^2)
CD = 2.2               # Drag coefficient (dimensionless)
DRAG_FACTOR = (CD * AREA) / MASS  # (m^2/kg)

# Assume a baseline radar that can detect a 10 cm object at 2000 km.
R_max_10cm = 2000.0  # km
