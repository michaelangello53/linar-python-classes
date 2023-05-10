import phonenumbers

from phonenumbers import geocoder,carrier,timezone
number=input('enter your number:')
phone_number=phonenumbers.parse(number)
print(f"location:{geocoder.description_for_number(phone_number, 'en')}")
print(f"carrier:{carrier.name_for_number(phone_number, 'en')}")
print(f"time zone:{timezone._country_level_time_zones_for_number(phone_number)}")