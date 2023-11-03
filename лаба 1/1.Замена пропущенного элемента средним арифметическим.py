numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
missing_item = 4
summ = sum(numbers[: missing_item]) + sum(numbers[missing_item + 1:])
len_ = len(numbers)
ср_ар_ = summ / len_
numbers[missing_item] = ср_ар_
print("Измененный список:", numbers)
