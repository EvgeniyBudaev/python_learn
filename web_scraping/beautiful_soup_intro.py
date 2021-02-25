from bs4 import BeautifulSoup # парсить html код
html_string = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Web Scraping</title>
</head>
<body>

  <h1>Hello, World!</h1>
  <h3>Programming Languages</h3>
  <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nobis, doloremque.</p>
  <ol>
    <li class="list__item">HTML</li>
    <li id="css-li">CSS</li>
    <li class="list__item">JavaScript</li>
    <li class="list__item">Python</li>
  </ol>
  
</body>
</html>
"""


parsed_html = BeautifulSoup(html_string, 'html.parser')
print(parsed_html)
print(type(parsed_html))
print(parsed_html.body.h1)
print(parsed_html.find('li'))
print('all li: ', parsed_html.find_all('li')) 
print(parsed_html.find(id="css-li")) # поиск по id
print('select по id: ', parsed_html.select("#css-li"))  # список
print(parsed_html.find(class_="list__item")) # поиск по классу
print('select по class: ', parsed_html.select(".list__item")) # список
print('select по class: ', parsed_html.select(".list__item")[0])