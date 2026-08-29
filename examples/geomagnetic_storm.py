from scripts.orbital_decay import simulate_decay

initial_h = 210  # km (Starlink Feb 2022 deployment altitude)
simulation_days = 10 

print(f"Simulating {simulation_days} days of orbital decay from {initial_h} km...")

# Scenario A: Quiet space weather
t_normal, h_normal = simulate_decay(initial_h, simulation_days, storm_start_day=None)

# Scenario B: Geomagnetic storm hits on Day 1 (mimicking Feb 3, 2022)
t_storm, h_storm = simulate_decay(initial_h, simulation_days, storm_start_day=1.0)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t_normal, h_normal, label='Normal Space Weather', color='green', linewidth=2)
plt.plot(t_storm, h_storm, label='G1 Geomagnetic Storm (Starts Day 1)', color='red', linewidth=2, linestyle='--')

# Formatting
plt.title("VLEO Orbital Decay: Normal vs. Geomagnetic Storm", fontsize=14)
plt.xlabel("Time (Days)", fontsize=12)
plt.ylabel("Altitude (km)", fontsize=12)
plt.axhline(80, color='black', linestyle=':', label='Approx. Re-entry Altitude (80 km)')
plt.axvline(1.0, color='orange', linestyle=':', label='Storm Onset (Day 1)')
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)
plt.xlim(0, simulation_days)
plt.ylim(0, initial_h + 20)

# Add annotation for the Starlink event
plt.annotate('Starlink Feb 2022:\n38 of 49 sats lost\nin similar conditions', 
             xy=(4, 100), xytext=(5, 130),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
             fontsize=10, bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.3))

plt.tight_layout()
plt.show()

# Print final stats
print(f"\n--- RESULTS ---")
print(f"Normal Altitude after {simulation_days} days: {h_normal[-1]:.1f} km")
print(f"Storm Altitude after {simulation_days} days:  {h_storm[-1]:.1f} km (Re-entered: {h_storm[-1] < 80})")
