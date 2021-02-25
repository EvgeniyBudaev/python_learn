import requests
url = 'https://www.google.com'
response = requests.get(url)
print(f'Request to {url}. Status code is {response.status_code}') # Request to https://www.google.com. Status code is 200
print(response.text) # получаем весь html