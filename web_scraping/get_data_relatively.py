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
    <li class="list__item" id="css-li">CSS</li>
    <li class="list__item bold">JavaScript</li>
    <li class="list__item python" id="python-li">Python</li>
  </ol>
  
</body>
</html>
"""

parsed_html = BeautifulSoup(html_string, 'html.parser')
data = parsed_html.body.contents # список элементов
print('data: ', data)
h1 = parsed_html.body.contents[1]
ol = parsed_html.body.contents[7].contents
print('ol: ', ol)
nextEl = parsed_html.body.contents[1].next_sibling.next_sibling
print('nextEl: ', nextEl) # <h3>Programming Languages</h3>

# find parent
parent_el = parsed_html.find(id='css-li').parent
print('parent_el: ', parent_el) 
prevEl = parsed_html.find(id='css-li').parent.previous_sibling.previous_sibling
print('prevEl: ', prevEl)

# Методы
findNextSibling = parsed_html.find(id='css-li').find_next_sibling() # пустые строки не учитываются
print('findNextSibling:', findNextSibling)
findPreviousSibling = parsed_html.find(id='css-li').find_previous_sibling()

elToAttrId = parsed_html.find(id='css-li').find_next_sibling(id="python-li")
elToAttrClass = parsed_html.find(id='css-li').find_next_sibling(class_="python")
print('elToAttrClass:', elToAttrClass)
parentElToAttrClass = parsed_html.find(id='css-li').find_next_sibling(class_="python").find_parent()

findChildren = parsed_html.body.findChildren # Поиск потомков => список всех потомков
findChildren2 = parsed_html.body.findChildren[2].find_next_sibling()