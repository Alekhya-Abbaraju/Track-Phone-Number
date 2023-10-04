import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium
mykey = "6d6f969fd9024ac8afde957f0c86a5ba" #open https://opencagedata.com/
number = "+919876543210" 
check = phonenumbers.parse(number)
numb_location = geocoder.description_for_number(check, "en")
service_provider = phonenumbers.parse(number)
service_provider_name = carrier.name_for_number(service_provider, "en")
geocoder = OpenCageGeocode(mykey)
query = str(numb_location)
results = geocoder.geocode(query)

lattitude = results[0]['geometry']['lat']
longitude = results[0]['geometry']['lng']
print("Location:", numb_location)
print("Service Provider:", service_provider_name)
print("Latitude:", lattitude)
print("Longitude:", longitude)
map_location = folium.Map(location=[lattitude, longitude], zoom_start=9)
folium.Marker([lattitude, longitude], popup=numb_location).add_to(map_location)
map_location.save("mylocation.html")
