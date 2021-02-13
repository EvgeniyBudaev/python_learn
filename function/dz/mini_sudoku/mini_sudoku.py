def any_duplicates(square):
    # ваше решение
    plain = [i for x in square for i in x]
    return sorted(plain) != [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(any_duplicates([[1, 1, 2], [9, 7, 8], [4, 5, 6]]))
    