# http://quotes.toscrape.com/

import requests
from bs4 import BeautifulSoup

response = requests.get('http://quotes.toscrape.com/')
# print(response.text)

html_data = BeautifulSoup(response.text)
quotes = html_data.find_all(class_="quote")
print('=======================')
# print('quotes:', quotes)
for quote in quotes:
  print(quote.find(class_="text").get_text()) # получили весь текст всех цитат
  print(quote.find(class_="author").get_text())
  print(quote.find(class_="keywords")['content'])