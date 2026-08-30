import numpy as np
from constants.constants import R_E

def computeSlantRange(R_obs, altitude, RA_deg, Dec_deg):
  R_obs_mag = np.linalg.norm(R_obs)
  
  # Assume the satellite is in a circular orbit (e.g., ISS at ~420 km altitude)
  #R_E = 6378.137 # Earth radius (km)
  r_sat = R_E + altitude # Target orbital radius (km)
  
  # Convert to radians
  RA_rad = np.radians(RA_deg)
  Dec_rad = np.radians(Dec_deg)
  
  # Calculate the Line-of-Sight (LOS) unit vector (rho_hat) in ECI
  rho_hat = np.array([
      np.cos(Dec_rad) * np.cos(RA_rad),
      np.cos(Dec_rad) * np.sin(RA_rad),
      np.sin(Dec_rad)
  ])
  
  
  # Equation: rho^2 + 2*(R_obs . rho_hat)*rho + (|R_obs|^2 - r_sat^2) = 0
  A = 1.0
  B = 2.0 * np.dot(R_obs, rho_hat)
  C = np.dot(R_obs, R_obs) - r_sat**2
  
  discriminant = B**2 - 4*A*C
  
  print("--- ANGLES-ONLY ORBIT DETERMINATION ---")
  print(f"Observer ECI Radius: {R_obs_mag:.2f} km")
  print(f"Assumed Orbit Radius: {r_sat:.2f} km")
  print(f"Line of Sight (RA={RA_deg}°, Dec={Dec_deg}°)\n")
  
  if discriminant < 0:
      print("ERROR: No real solution. The telescope is pointing away from the assumed orbit.")
  else:
      rho1 = (-B + np.sqrt(discriminant)) / (2*A)
      rho2 = (-B - np.sqrt(discriminant)) / (2*A)
      
      # Filter for positive slant ranges (distance cannot be negative)
      valid_rhos = [r for r in [rho1, rho2] if r > 0]
      
      if not valid_rhos:
          print("ERROR: Line of sight points away from the satellite.")
      else:
          # If the line pierces the spherical orbit shell twice, take the closer intersection.
          rho = min(valid_rhos) 
          
          print(f"Calculated Slant Range (rho): {rho:.2f} km")
          return rho
          
          # Calculate the final 3D ECI position of the satellite
          R_sat_vec = R_obs + rho * rho_hat
          
          print(f"\n--- RECONSTRUCTED SATELLITE STATE ---")
          print(f"Satellite ECI Position: X={R_sat_vec[0]:.2f}, Y={R_sat_vec[1]:.2f}, Z={R_sat_vec[2]:.2f} km")
          print(f"Verification - Orbital Radius: {np.linalg.norm(R_sat_vec):.2f} km")
