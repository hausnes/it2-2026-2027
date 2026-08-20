import requests

url = 'https://biapi.nve.no/nettleiestatistikk/swagger/v1/swagger.json'
r = requests.get(url)

# Parse JSON-responsen
data = r.json()

print(data['paths'])