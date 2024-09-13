def find_unique_value(some_list: list[int]) -> list[int]:
    return [number for number in some_list if some_list.count(number) == 1]
print(find_unique_value([2, 3, 4, 2, 2, 3, 4, 5]))
print(find_unique_value([1, 2, 1, 1]))
print(find_unique_value([2, 3, 3, 3, 5, 5]))
print(find_unique_value([5, 5, 5, 2, 2, 0.5]))
print("ОК")
