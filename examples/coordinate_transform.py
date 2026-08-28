import astropy.units as u
from astropy.coordinates import EarthLocation, AltAz, GCRS, ITRS, CartesianRepresentation
from astropy.time import Time

# ==========================================
# 1. DEFINE THE "WHEN" AND "WHERE" (GROUND)
# ==========================================
# Current observation time (UTC)
obs_time = Time('2026-08-28 15:00:00', scale='utc')

# Define our ground observer's location (e.g., Cape Canaveral, FL)
# Latitude, Longitude, and Height above the WGS84 ellipsoid
observer_loc = EarthLocation(lat=28.5*u.deg, lon=-80.6*u.deg, height=0*u.m)

# ==========================================
# 2. DEFINE THE SATELLITE IN ECI (GCRS)
# ==========================================
# Let's invent a satellite in Low Earth Orbit (LEO).
# We define its position in Cartesian coordinates (X, Y, Z) in kilometers.
# Because GCRS is ECI, this position is fixed relative to the stars.
sat_pos_eci = CartesianRepresentation(x=4500*u.km, y=5500*u.km, z=3500*u.km)

# Create the ECI coordinate object
sat_gcrs = GCRS(sat_pos_eci, obstime=obs_time)

# ==========================================
# 3. CONVERT ECI -> ECEF (ITRS)
# ==========================================
# Astropy handles the complex Earth-rotation math (polar motion, precession, 
# nutation, and Earth rotation angle) automatically when transforming to ITRS.
sat_itrs = sat_gcrs.transform_to(ITRS(obstime=obs_time))

# ==========================================
# 4. CONVERT ECEF -> TOPOCENTRIC (AltAz)
# ==========================================
# Now we calculate the Azimuth and Elevation from our specific ground station.
sat_altaz = sat_itrs.transform_to(AltAz(obstime=obs_time, location=observer_loc))

# ==========================================
# 5. PRINT THE RESULTS
# ==========================================
print("--- SATELLITE POSITION ANALYSIS ---")
print(f"Time of Observation (UTC): {obs_time.utc.iso}")
print(f"Observer Location: Cape Canaveral (28.5°N, 80.6°W)\n")

print("1. ECI (GCRS) - Inertial Space [km]:")
print(f"   X: {sat_gcrs.cartesian.x.to(u.km):.2f}")
print(f"   Y: {sat_gcrs.cartesian.y.to(u.km):.2f}")
print(f"   Z: {sat_gcrs.cartesian.z.to(u.km):.2f}\n")

print("2. ECEF (ITRS) - Earth-Fixed [km]:")
print(f"   X: {sat_itrs.cartesian.x.to(u.km):.2f}")
print(f"   Y: {sat_itrs.cartesian.y.to(u.km):.2f}")
print(f"   Z: {sat_itrs.cartesian.z.to(u.km):.2f}\n")

print("3. Topocentric (AltAz) - Observer View:")
print(f"   Azimuth:   {sat_altaz.az.deg:.2f} degrees")
print(f"   Elevation: {sat_altaz.alt.deg:.2f} degrees")
