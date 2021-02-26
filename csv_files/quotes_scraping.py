# http://quotes.toscrape.com/

import requests
from bs4 import BeautifulSoup
import csv

response = requests.get('http://quotes.toscrape.com/')
html_data = BeautifulSoup(response.text)
quotes = html_data.find_all(class_="quote")

with open('/Users/evgeniybudaev/Documents/CODE/PYTHON/Ilia Fofanov/python_learn/csv_files/csv_quotes_writer.csv', 'w') as file: 
  csv_writer = csv.writer(file)
  csv_writer.writerow(['Text', 'Author', 'Keywords'])

  for quote in quotes:
    text = quote.find(class_="text").get_text()
    author = quote.find(class_="author").get_text()
    keywords = quote.find(class_="keywords")['content']
    csv_writer.writerow([text, author, keywords])