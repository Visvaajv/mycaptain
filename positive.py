def print_positive_numbers(lst):
    positive_numbers = [num for num in lst if num > 0]
    print("Output:", positive_numbers)

list1 = [12, -7, 5, 64, -14]
print("Input:", list1, end=" ")
print_positive_numbers(list1)

list2 = [12, 14, -95, 3]
print("Input:", list2, end=" ")
print_positive_numbers(list2)
