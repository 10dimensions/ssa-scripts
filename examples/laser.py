import numpy as np
import matplotlib.pyplot as plt
from constants.constants import c

target_distance = 6000000.0 # 6000 km to LAGEOS (one-way)

# Round trip distance
round_trip = target_distance * 2

# Time of flight for the laser pulse
time_of_flight = round_trip / c
print(f"--- SLR TO LAGEOS ---")
print(f"Round-trip light time: {time_of_flight:.6f} seconds ({time_of_flight*1000:.2f} ms)\n")

# How much time error corresponds to 1 millimeter of range error?
range_error = 0.001 # 1 millimeter
time_error = (range_error * 2) / c

print(f"To achieve 1 mm range accuracy...")
print(f"Your clock must be accurate to: {time_error:.12f} seconds")
print(f"Which is: {time_error * 1e12:.2f} picoseconds!\n")
print("This is why SLR stations use ultra-precise atomic clocks and picosecond lasers.\n")


# Let's simulate 100 observations of a satellite passing overhead.
# We will plot the "Residuals" (the difference between the measured 
# data and the true mathematical orbit).

np.random.seed(42)
time_steps = np.arange(0, 100)

# Radar Data: Good, but has a slight bias (e.g. 3 meters) and random noise (~2 meters)
radar_residuals = 3.0 + np.random.normal(0, 2.0, 100)

# SLR Data: Near-zero bias, incredibly tight noise (~3 millimeters)
slr_residuals = 0.005 + np.random.normal(0, 0.003, 100)

plt.figure(figsize=(10, 6))
plt.scatter(time_steps, radar_residuals, c='red', label='Radar Residuals', alpha=0.6, s=30)
plt.plot(time_steps, slr_residuals, c='blue', label='SLR Residuals (Normal Points)', linewidth=2)

plt.axhline(0, color='black', linestyle='--', label='Perfect True Orbit')
plt.title("Orbit Determination Residuals: Radar vs. SLR", fontsize=14)
plt.xlabel("Observation Time (Minutes)", fontsize=12)
plt.ylabel("Range Residual Error (Meters)", fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)

# Annotate the difference
plt.annotate('Radar Bias\n(~3m off)', xy=(50, 3), xytext=(60, 6),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, color='red')

plt.tight_layout()
plt.show()
