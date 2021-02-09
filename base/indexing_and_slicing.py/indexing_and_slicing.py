text = "Hello Python!"
text_length = len(text)
print('Длинна: ', text_length)
print("Hello Python!"[3])

# Indexing
print(text[0])

# Slicing
print(text[1:4])
print(text[1:]) # вырезаем с индекса 1 включительно и до конца строки
print(text[:4]) # вырезаем по индекс 3 включительно с начала строки
print(text[::2]) # с индекса 0 с шагом 2 вырезаем символы
print(text[1:9:2]) # с 1 по 8 с шагом 2
print(text[::-1]) # перевернутая строка

