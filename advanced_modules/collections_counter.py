from collections import Counter

number_list = [11, 11, 13, 15, 15]
string = 'dddaac'
sentence = 'Hello, how are you doing? Hello, i am fine. How do you do?'

print(Counter(number_list)) # Counter({11: 2, 15: 2, 13: 1})
print(Counter(string)) # Counter({'d': 3, 'a': 2, 'c': 1})
print(Counter(sentence.split(' '))) # Counter({'Hello,': 2, 'you': 2, 'how': 1, 'are': 1, 'doing?': 1, 'i': 1, 'am': 1, 'fine.': 1, 'How': 1, 'do': 1, 'do?': 1})

c = Counter(sentence.split(' '))
print(sum(c.values())) # 13 элементов
# c.clear() # 0 очистка счетчика
print(list(c)) # ['Hello,', 'how', 'are', 'you', 'doing?', 'i', 'am', 'fine.', 'How', 'do', 'do?']
print(set(c))
print(dict(c))
print(c.items())
c = Counter(dict(c))
print(c.most_common(2)) # 2 часто встречающихся элемента
print(c.most_common(2)[:-3-1:-1]) # 3 редко встречающиеся элементы 