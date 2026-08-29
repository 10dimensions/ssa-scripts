import numpy as np
import matplotlib.pyplot as plt
from skyfield.api import load, wgs84

def sgp4Propagate(station, times):
  # The ISS is typically the first object in the 'stations' group
  # station = stations[id]  
  print(f"Loaded: {station.name} (NORAD ID: {station.model.satnum})")
  
  #ts = load.timescale()
  
  # Generate 1000 time steps between midnight and midnight the next day (UTC)
  #times = ts.utc(2026, 8, 28, np.linspace(0, 24, 1000))
  
  geocentric = iss.at(times)
  return geocentric


def plotGroundTrack(geocentric):
  # Convert the 3D space position into a subpoint (Lat/Lon on Earth's surface)
  subpoint = wgs84.subpoint_of(geocentric)
  
  lats = subpoint.latitude.degrees
  lons = subpoint.longitude.degrees
  
  plt.figure(figsize=(12, 6))
  
  # We use scatter() instead of plot() 
  # when the orbit crosses the International Date Line (from +180 to -180 longitude).
  plt.scatter(lons, lats, s=2, c='red', alpha=0.8) 
  
  plt.title("ISS 24-Hour Ground Track (Propagated via SGP4)")
  plt.xlabel("Longitude (degrees)")
  plt.ylabel("Latitude (degrees)")
  plt.xlim(-180, 180)
  plt.ylim(-90, 90)
  plt.grid(True, linestyle='--', alpha=0.5)
  plt.axhline(0, color='black', linewidth=1)  # Equator
  plt.axvline(0, color='black', linewidth=1)  # Prime Meridian
  plt.show()
