import numpy as np
import matplotlib.pyplot as plt
from constants.constants import R_max_10cm 

# Optical Region Assumption (RCS scales with d^2)
# R_max is proportional to (d^2)^(1/4) = d^(1/2)
def computeRadarRangeOptical(diameters_cm):
  R_optical = R_max_10cm * np.sqrt(diameters_cm / 10.0)
  return R_optical

# Rayleigh Region Reality (RCS scales with d^6)
# R_max is proportional to (d^6)^(1/4) = d^(1.5)
def computeRadarRangeRayleigh(diameters_cm):
  R_rayleigh = R_max_10cm * ((diameters_cm / 10.0) ** 1.5)
  return R_rayleigh

def plotRadarRange(diameters_cm, R_optical,R_rayleigh):
  plt.figure(figsize=(10, 6))
  plt.plot(diameters_cm, R_optical, marker='o', label='Optical Region Model ($R \propto d^{0.5}$)', linewidth=2)
  plt.plot(diameters_cm, R_rayleigh, marker='s', label='Rayleigh Region Reality ($R \propto d^{1.5}$)', linewidth=2, color='red')
  
  plt.title("Radar Detection Range vs. Debris Size (S-Band)", fontsize=14)
  plt.xlabel("Debris Diameter (cm)", fontsize=12)
  plt.ylabel("Max Detection Range (km)", fontsize=12)
  plt.xscale('log')  # Log scale for diameter makes the drop-off clear
  plt.yscale('log')
  plt.grid(True, which="both", ls="--", alpha=0.6)
  plt.legend(fontsize=11)
  
  # Annotate the 1cm mark
  plt.axvline(x=1, color='gray', linestyle=':', linewidth=1.5)
  plt.annotate('1 cm Debris\n(Rayleigh Region)', xy=(1, R_rayleigh[3]*1.5), 
               xytext=(2, R_rayleigh[3]*3),
               arrowprops=dict(facecolor='black', shrink=0.05, width=1))
  
  plt.tight_layout()
  plt.show()
