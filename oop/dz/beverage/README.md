ДЗ-6:  Смузи

Создать класс Beverage, который при конструировании принимает список ингредиентов

1) поддерживает атрибут ingredients, возвращающий список ингредиентов, переданных при конструировании инстанции класса
2) поддерживает функцию get_cost, вычисляющую итоговую стоимость всех ингредиентов напитка (получается себестоимость напитка)
3) поддерживает функцию get_price, вычисляющую цену напитка посредством умножения себестоимости на 2.5
4)поддерживает функцию get_name, которая возвращает строку, перечисляющую ингредиенты, сортируя их в алфавитном порядке. Если ингредиентов больше одного, то в конце добавляет слово 'Fusion', иначе добавляет слово 'Smoothie'. Эта функция также должна заменять 'berries' на 'berry'.

Ингредиенты и их себестоимость
Strawberries $1.50
Banana $0.50
Mango $2.50
Blueberries $1.00
Raspberries $1.00
Apple $1.75
Pineapple $3.50

Примеры вызовов

s1 = Beverage(["Banana"])
s1.ingredients -> ["Banana"]
s1.get_cost() -> "$0.50"
s1.get_price() -> "$1.25"
s1.get_name() -> "Banana Smoothie"

s2 = Beverage(["Raspberries", "Strawberries", "Blueberries"])
s2.ingredients -> ["Raspberries", "Strawberries", "Blueberries"]
s2.get_cost() -> "$3.50"
s2.get_price() -> "$8.75"
s2.get_name() -> "Blueberry Raspberry Strawberry Fusion "