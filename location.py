from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geo_app")
location = geolocator.geocode("Dhaka")
print("Address",location.address)
print("Cordinates",(location.latitude,location.longitude))