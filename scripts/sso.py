import numpy as np
from constants.constants import mu, R_E, J2

def computeInclination(altitude):
  #altitude = 700        # km
  a = R_E + altitude    # km
  
  # Mean motion (rad/s -> deg/day)
  n_rad_s = np.sqrt(mu / a**3)
  n_deg_day = n_rad_s * (180 / np.pi) * 86400
  
  # Target nodal regression for SSO (deg/day)
  target_Omega_dot = 360 / 365.2422 
  
  # Solve for inclination
  cos_i = target_Omega_dot / (-1.5 * J2 * (R_E / a)**2 * n_deg_day)
  inclination_deg = np.degrees(np.arccos(cos_i))
  
  print(f"Required SSO Inclination at {altitude} km altitude: {inclination_deg:.2f}°")

  return inclination_deg 
