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
    <li class="list__item">Python</li>
  </ol>
  
</body>
</html>
"""

parsed_html = BeautifulSoup(html_string, 'html.parser')
html_elem = parsed_html.select('li')[0]
print(html_elem.get_text()) # получение текста из элемента

# html_elem_list = parsed_html.select('.list__item')
html_elem_list = parsed_html.select('li') # получение текста из списка элементов
for html_el in html_elem_list:
  print(html_el.get_text())
  print(html_el.name) # названия элементов
  print(html_el.attrs)


html_elem_list2 = parsed_html.select('li')[1]
print(html_elem_list2.attrs['class'])
print(html_elem_list2['id'])   