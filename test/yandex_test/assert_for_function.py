def movie_quotes(name):
    """Возвращает цитаты известных персонажей из фильмов."""
    quotes = {
        'Элли': 'Тото , у меня такое ощущение, что мы не в Канзасе!',
        'Шерлок': 'Элементарно, Ватсон!',
        'Дарт Вейдер': 'Я — твой отец.',
        'Thomas A. Anderson': 'Меня. Зовут. Нео!',
        'Алиса Плезенс Лидделл': 'Всё чудесатее и чудесатее!'
    }
    return quotes.get(name, 'Персонаж пока не известен миллионам.')

# Утверждаем, что если в movie_quotes() передать 'Шерлок' -
# функция вернёт 'Элементарно, Ватсон!'.
assert movie_quotes('Шерлок') == 'Элементарно, Ватсон!', (
   "movie_quotes('Шерлок') не вернул ожидаемый результат!")

# Утверждаем, что если в movie_quotes() передать 'Thomas A. Anderson' -
# функция вернёт 'Меня зовут Нео!'.
assert movie_quotes('Thomas A. Anderson') == 'Меня. Зовут. Нео!', (
    "movie_quotes('Thomas A. Anderson') не вернул ожидаемый результат!")

# Утверждаем, что если в movie_quotes передать 'Алиса Плезенс Лидделл' -
# функция вернёт 'Всё чудесатее и чудесатее!'.
expected_answer = 'Всё чудесатее и чудесатее!'
assert movie_quotes('Алиса Плезенс Лидделл') == expected_answer, (
    "movie_quotes('Алиса Плезенс Лидделл') не вернул ожидаемый результат!")


#  Задача
def series_sum(incoming):
    # Конкатенирует все элементы списка, приводя их к строкам."
    result = ''
    for i in incoming:
        result += str(i)
    return result

mixed_numbers = [1, 4.5, 8]
result_numbers = series_sum(mixed_numbers)
print('result_numbers', result_numbers)
mixed_numbers_strings = [1, 'a', 8]
result_numbers_strings = series_sum(mixed_numbers_strings)
print('result_numbers_strings', result_numbers_strings)
empty = []
result_empty = series_sum(empty)
print('result_empty', result_empty)


assert series_sum(mixed_numbers) == '14.58', (
    'Функция series_sum() не работает со списком чисел')


assert series_sum(mixed_numbers_strings) == '1a8', (
    'Функция series_sum() не работает со смешанным списком')


assert series_sum(empty) == '', (
    'Функция series_sum() не работает с пустым списком')
