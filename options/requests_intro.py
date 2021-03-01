import requests
from requests import HTTPError

try:
  response = requests.get("https://www.engineerspock.com/")
  print(response.status_code) # 200
except HTTPError as http_err:
  print(f'Error: {http_err}')
except Exception as err:
  print(f'Unknow error: {err}') 
else:
  print("connected Successfully!")   


# ===
print(response.content)
response.encoding = 'utf-8'
print(response.text)

# ===
github_response = requests.get("https://api/github.com")
data = github_response.json() # распарсить json
print(data)

blog_response = requests.get("https://www.engineerspock.com/")
github_api_response = requests.get("https://api/github.com")
print(blog_response.headers, end="\n")
print('')
print(github_api_response.headers, end="\n")
print(blog_response.headers["content-type"])

# ===
placeholder_response = requests.get("http://jsonplaceholder.typicode.com/comments", params=b'postId=1')
print(placeholder_response.json())

# ===
bin_response = requests.post("https://httpbin.org/post", json=json_data)
bin_json_response = bin_response.json()
print(bin_json_response['data'])

# ===
from getpass import getpass
auth_response = requests.get("https://api.github.com/user", auth=("engineerSpock", getpass()))
print(auth_response.json())

# ===
from requests.exceptions import Timeout

try:
  response = requests.get("https://www.engineerspock.com/", timeout = 1)
except Timeout:
  print("The request timed out")

with requests.Session() as session:
  session.auth = ("EngineerSpock", getpass())
  response = session.get("https://api.github.com/user")
print(response.json())  

# === прописать количество повторений для запроса, если он провалился
from requests.adapters import HTTPAdapter
adapter = HTTPAdapter(max_retries=3) # 3 - количество попыток создать запрос
with requests.Session() as session:
  session.mount('https://api.github.com/', adapter)
  session.auth = ("EngineerSpock", getpass())
  try:
    session.get("https://api.github.com/user")
  except ConnectionError as err:
    print(f'Failed to connect: {err}')
  else:
    print('OK')   


  