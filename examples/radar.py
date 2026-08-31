from scripts.radar_csa import computeRadarRangeOptical, computeRadarRangeRayleigh, plotRadarRange

# Print the stark reality
print("--- RADAR DETECTION REALITY CHECK ---")
# Diameters to test (in cm)
diameters_cm = np.array([10, 5, 2, 1, 0.5, 0.1])

print(f"Baseline: 10 cm object detected at {R_max_10cm} km")

R_optical = computeRadarRangeOptical(diameters_cm)
print(f"1 cm object (Optical Model): Detectable at {R_optical[3]:.1f} km")

R_rayleigh = computeRadarRangeRayleigh(diameters_cm)
print(f"1 cm object (Rayleigh Reality): Detectable at ONLY {R_rayleigh[3]:.1f} km")

plotRadarRange(diameters_cm, R_optical,R_rayleigh)
