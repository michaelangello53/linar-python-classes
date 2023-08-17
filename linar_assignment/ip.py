import requests

def get_public_ip_address():
    response = requests.get('https://api.ipify.org?format=json')
    data = response.json()
    ip_address = data['ip']
    return ip_address

ip_address = get_public_ip_address()
print("Public IP Address:", ip_address)