import geocoder
g = geocoder.ip('me')
print(g.latlng)
# %load_ext autotime
import pandas as pd
import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import matplotlib.pyplot as plt
import plotly_express as px
import tqdm
from tqdm.notebook import tqdm_notebook

locator = Nominatim(user_agent="myGeocoder")
coordinates = "53.480837, -2.244914"
coordinates ="{},{}".format(g.latlng[0],g.latlng[1])
location = locator.reverse(coordinates)
print (location.raw)