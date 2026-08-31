import numpy as np
import astropy.units as u
from poliastro.bodies import Earth
from poliastro.twobody import Orbit
from poliastro.iod import gibbs


# Let's create a known LEO satellite to act as our "ground truth"
# Altitude = 500 km, Circular (e=0), Inclination = 45 degrees
a_true = (Earth.R + 500 * u.km).to(u.km)
ecc_true = 0.0 * u.one
inc_true = 45.0 * u.deg
raan_true = 0.0 * u.deg
argp_true = 0.0 * u.deg
nu_true = 0.0 * u.deg

orbit_true = Orbit.from_classical(Earth, a_true, ecc_true, inc_true, raan_true, argp_true, nu_true)

# We will "observe" the satellite at t=0s, t=300s, and t=600s.
# (For Gibbs' method, observations should be separated by ~5 to 15 degrees of true anomaly)
t1 = 0 * u.s
t2 = 300 * u.s
t3 = 600 * u.s

# Extract the position (r) and velocity (v) vectors at these times
r1, v1 = orbit_true.propagate(t1).rv()
r2, v2_true = orbit_true.propagate(t2).rv()
r3, v3 = orbit_true.propagate(t3).rv()

print("--- SIMULATED RADAR OBSERVATIONS (ECI Position Vectors) ---")
print(f"Observation 1 (t=0s):   r1 = {r1}")
print(f"Observation 2 (t=300s): r2 = {r2}")
print(f"Observation 3 (t=600s): r3 = {r3}\n")


# We pretend we DON'T know the velocity. We only feed the 3 position vectors into Gibbs.
# Gibbs returns the calculated velocity vector at the MIDDLE observation (v2).
v2_iod = gibbs(Earth, r1, r2, r3)

# Now we combine the known middle position (r2) with our calculated velocity (v2_iod)
orbit_iod = Orbit.from_vectors(Earth, r2, v2_iod)

print("--- IOD RESULTS (Gibbs' Method) vs TRUE ORBIT ---")
print(f"{'Orbital Element':<18} | {'True Orbit':<15} | {'IOD Orbit':<15} | {'Error'}")
print("-" * 70)

# Extract elements from the IOD orbit
a_iod = orbit_iod.a
ecc_iod = orbit_iod.ecc
inc_iod = orbit_iod.inc
raan_iod = orbit_iod.raan
argp_iod = orbit_iod.argp

print(f"Semi-major axis  | {a_true.to(u.km):<15.2f} | {a_iod.to(u.km):<15.2f} | {(a_iod - a_true).to(u.km):.2f} km")
print(f"Eccentricity     | {ecc_true:<15.4f} | {ecc_iod:<15.4f} | {ecc_iod - ecc_true:.4f}")
print(f"Inclination      | {inc_true.to(u.deg):<15.2f} | {inc_iod.to(u.deg):<15.2f} | {(inc_iod - inc_true).to(u.deg):.2f} deg")
print(f"RAAN             | {raan_true.to(u.deg):<15.2f} | {raan_iod.to(u.deg):<15.2f} | {(raan_iod - raan_true).to(u.deg):.2f} deg")
print(f"Arg of Perigee   | {argp_true.to(u.deg):<15.2f} | {argp_iod.to(u.deg):<15.2f} | {(argp_iod - argp_true).to(u.deg):.2f} deg")
