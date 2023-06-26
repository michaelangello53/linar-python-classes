"""import time
def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
input("Press Enter to start")
start_time = time.time()
input("Press Enter to stop")
end_time = time.time()
time_lapsed = end_time - start_time
time_convert(time_lapsed)"""

import requests
def get_location(phone_number):
    api_key = "6ABHWBNHtGr0rQFk7vWS8pmmwWhJwVX4"  # Replace with your actual API key
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}&country_code=&format=1"

    response = requests.get(url)
    data = response.json()

    print(data)  # Add this line to inspect the response

    if data.get('valid'):
        location = data['country_name']
        return location
    else:
        return "Phone number is not valid."

# Example usage
phone_number = "+2347068298347"  # Replace with the phone number you want to lookup
location = get_location(phone_number)
print(f"Location: {location}")