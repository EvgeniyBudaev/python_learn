class Calculator:
    """Производит арифметические действия."""
    def summ(self, *args):
        """Возвращает сумму принятых аргументов."""
        if len(args) < 2:
            return None
        sum = 0
        for i in args:
            sum += i
        return sum

    def divider(self, num1, num2):
        """Возвращает результат деления num1 / num2."""
        return num1 / num2

    def square(self, num):
        """Возвращает квадратный корень аргумента."""
        if num < 0:
            raise ValueError('Не могу извлечь корень из отрицательного числа')
        return num ** 0.5
