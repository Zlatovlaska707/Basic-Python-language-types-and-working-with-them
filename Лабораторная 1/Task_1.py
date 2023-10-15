numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
# Находим индекс элемента со значением None
index_none = numbers.index(None)

# Вычисляем среднее арифметическое значений, исключая None
# Заменяем None на вычисленное среднее арифметическое
numbers[index_none] = (round((sum(numbers[:index_none])+sum(numbers[index_none+1:]))/(len(numbers)), 2))
print("Измененный список:", numbers)
