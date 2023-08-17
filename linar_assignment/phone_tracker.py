"""import phonenumbers
import opencage
import folium
from phonenumbers import geocoder
ch_number = phonenumbers.parse("+2347068298347", "CH")
print(geocoder.description_for_number(ch_number, "en"))
from phonenumbers import carrier
service_provider = phonenumbers.parse("+2347068298347", "RO")
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
key="d0404fa840f143188cc0e30ce60b9ec1"
geocoder=OpenCageGeocode(key)
query=str(ch_number)
results=geocoder.geocode(query)
#print(results)

lat=results [0]['geometry']['lat']
lng=results [0]['geometry']['lng']

print(lat,lng)

mymap=folium.map(ch_number=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=ch_number).add_to(mymap)
mymap.save("mylocation.py")"""


import requests
import json
ip=input('Enter ip address:')
host=json.loads(requests.get(f'https://ipinfo.io/{ip}/json').content)


ip=host['ip']
city=host['city']
region=host['region']
country=host["country"]
timezone=host["timezone"]


print(f'ip Address:{ip}')
print(f'ip City:{city}')
print(f'ip Region:{region}')
print(f'ip Country:{country}')
print(f'ip Timezone:{timezone}')