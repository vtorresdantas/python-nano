from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="wazeyes") # Nome do seu aplicativo
location = geolocator.geocode("Rua Jose Serdeira Ribas, 304")
print(location.address)
print((location.latitude, location.longitude))