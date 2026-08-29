import numpy as np
import matplotlib.pyplot as plt
from constants.constants import mu_m, R_E_m, H_REF, DENSITY_NORMAL_200KM, DENSITY_STORM_200KM, SCALE_HEIGHT_NORMAL, SCALE_HEIGHT_STORM, MASS, AREA, CD

def get_density(altitude_m, is_storm):
    """Calculates atmospheric density at a given altitude."""
    if is_storm:
        rho_0 = DENSITY_STORM_200KM
        H = SCALE_HEIGHT_STORM
    else:
        rho_0 = DENSITY_NORMAL_200KM
        H = SCALE_HEIGHT_NORMAL
    
    # Exponential atmosphere model: rho = rho_0 * exp(-(h - h_ref) / H)
    return rho_0 * np.exp(-(altitude_m - H_REF) / H)

# ==========================================
# 3. ORBITAL DECAY SIMULATION
# ==========================================
def simulate_decay(initial_altitude_km, days, storm_start_day=None):
    """
    Simulates orbital decay over a given number of days.
    """
    dt = 3600  # Time step: 1 hour (in seconds)
    total_steps = int(days * 24)
    
    altitudes_km = []
    times_days = []

    MU = mu_m
    R_E = R_E_m

    DRAG_FACTOR = (CD * AREA) / MASS  # (m^2/kg)
  
    # Initial state
    r = R_E + (initial_altitude_km * 1000)  # Initial orbital radius (m)
    
    for step in range(total_steps):
        current_day = step * dt / 86400
        
        # Determine if a storm is active
        is_storm = (storm_start_day is not None) and (current_day >= storm_start_day)
        
        altitude_m = r - R_E
        altitudes_km.append(altitude_m / 1000)
        times_days.append(current_day)
        
        # 1. Calculate orbital velocity (vis-viva equation for near-circular orbit)
        v = np.sqrt(MU / r)  # m/s
        
        # 2. Calculate atmospheric density at current altitude
        rho = get_density(altitude_m, is_storm)
        
        # 3. Calculate Drag Acceleration: a_d = 0.5 * (Cd * A / m) * rho * v^2
        a_drag = 0.5 * DRAG_FACTOR * rho * (v ** 2)  # m/s^2
        
        # 4. Calculate rate of change of orbital radius (dr/dt)
        # Derived from specific orbital energy: dE/dt = -a_drag * v
        # Since E = -MU / (2r), dE/dt = (MU / (2r^2)) * (dr/dt)
        # Therefore: dr/dt = - (r^2 / MU) * (Cd * A / m) * rho * v^3
        dr_dt = - (r ** 2 / MU) * DRAG_FACTOR * rho * (v ** 3)
        
        # 5. Update radius using Euler integration
        r = r + dr_dt * dt
        
        # Safety break: if satellite re-enters (< 80 km)
        if altitude_m < 80000:
            altitudes_km.append(altitude_m / 1000)
            times_days.append(current_day)
            break
            
    return times_days, altitudes_km
