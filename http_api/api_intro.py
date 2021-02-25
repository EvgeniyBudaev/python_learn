import requests

# url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-01-02'
# response = requests.get(url, headers={'Accept':'application/json'})

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
response = requests.get(url, headers={'Accept':'application/json'}, params={
  'format': 'geojson',
  'starttime': '2014-01-01',
  'endtime': '2014-01-02'
})

# print(response.text)
# print(response.json())
# print(type(response.json())) # dict
data = response.json()
print(data['features'][0]['properties']['place'])