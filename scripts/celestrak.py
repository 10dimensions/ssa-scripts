from skyfield.api import load

def fetchCelesTrakData():
  print("Fetching latest TLEs from CelesTrak API...")
  tle_url = 'https://celestrak.org/NORAD/elements/gp.php?GROUP=stations&FORMAT=tle'
  stations = load.tle_file(tle_url)
  return stations
