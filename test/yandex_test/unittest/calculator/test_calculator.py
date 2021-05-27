import sys
import os
import unittest

# Добавим возможность импорта из директории calculator в наш тест
sys.path.append(os.path.abspath('./calculator'))
from test.yandex_test.unittest.calculator.calculator import Calculator


class TestCalc(unittest.TestCase):
    """Тестируем Calculator."""

    @classmethod
    def setUp(cls):
        """Подготовка прогона теста. Вызывается перед каждым тестом."""
        # Arrange - подготавливаем данные для теста
        # Создаем экземпляр класса Calculator()
        cls.calc = Calculator()

    def test_summ(self):
        # summ возвращает сумму принятых аргументов
        # Act - выполнение тестируемого сценария.
        # Вызываем метод summ
        act = self.calc.summ(3, -3, 5)

        # Assert - проверяем, что метод работает
        self.assertEqual(act, 5, 'Метод summ работает неправильно')

    def test_square(self):
        # square() возвращает квадратный корень аргумента
        act = self.calc.square(4)
        self.assertEqual(act, 2, 'Метод square работает неправильно')

    # Корень из отрицательного числа не является действительным числом
    def test_square_negative_value(self):
        # Проверяем, что при вызове с отрицательным числом
        # выбрасывается исключение ValueError
        # assertRaises обрабатывается с помощью менеджера контекста with
        with self.assertRaises(ValueError):
            act = self.calc.square(-1)
