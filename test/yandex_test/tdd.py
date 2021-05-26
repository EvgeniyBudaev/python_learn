def test_sort(sorting_algorithm):
    """ Тестируем алгоритм, сортирующий список по возрастанию."""
    # Напечатать имя функции
    print(f'Тестируем функцию: {sorting_algorithm.__name__}')

    # Ваш код здесь
    source = [1, 3, 2.5, 4]
    inversed = [1, 2.5, 3, 4]
    assert sorting_algorithm(source) == inversed, (
        f"Алгоритм в {sorting_algorithm.__name__} работает неправильно со "
        f"списком, содержащим int и float '{source}'")

    source = [1, -5, 0, 4]
    inversed = [-5, 0, 1, 4]
    assert sorting_algorithm(source) == inversed, (
        f"Алгоритм в {sorting_algorithm.__name__} работает неправильно со "
        f"списком, содержащим отрицательные величины, нулевое значение '"
        f"{source}'")

    source = [5, 5, 5, 5]
    inversed = [5, 5, 5, 5]
    assert sorting_algorithm(source) == inversed, (
        f"Алгоритм в {sorting_algorithm.__name__} работает неправильно со "
        f"списком, содержащим одинаковые числа '{source}'")

    source = []
    inversed = []
    assert sorting_algorithm(source) == inversed, (
        f"Алгоритм в {sorting_algorithm.__name__} работает неправильно с "
        f"пустым списком '{source}'")

    print(f'Тест для {sorting_algorithm.__name__} пройден')

# Ипортируем тестируемые функции из пакета ttd_sprint5_data
# test_sort(ttd_sprint5_data.bubble_sort)
# test_sort(ttd_sprint5_data.timsort_sort)
# test_sort(ttd_sprint5_data.selection_sort)
# test_sort(ttd_sprint5_data.insertion_sort)
# test_sort(ttd_sprint5_data.cap_sort)
# test_sort(ttd_sprint5_data.merge_sort)
# test_sort(ttd_sprint5_data.heap_sort)
# test_sort(ttd_sprint5_data.stepa_sort)
# test_sort(ttd_sprint5_data.quick_sort)
# test_sort(ttd_sprint5_data.sus_sort)
