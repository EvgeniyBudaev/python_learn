class Calculator:
    """Производит арифметические действия."""
    def summ(self, *args):
        """Возвращает сумму принятых аргументов."""
        sum = 0
        for i in args:
            sum += i
        return sum

    def square(self, num):
        """Возвращает квадратный корень аргумента."""
        if num < 0:
            raise ValueError('Не могу извлечь корень из отрицательного числа')
        return num ** 0.5
