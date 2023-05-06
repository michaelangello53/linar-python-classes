import requests
import json
ip=input('Enter ip address:')

host=json.loads(requests.get(f'https://ipinfo.io/{ip}/json').content)
ip=host['ip']
city =host['city']
region =host['region']
country =host["country"]
timezone =host["timezone"]


print(f'ip Address:{ip}')
print(f'ip City:{city}')
print(f'ip Region:{region}')
print(f'ip Country:{country}')
print(f'ip Timezone:{timezone}')