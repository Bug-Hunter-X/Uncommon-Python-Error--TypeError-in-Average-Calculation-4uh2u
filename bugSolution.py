def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 #Handle list with non-numeric values
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_list = [10, 20, 30, 40, 50]
result = calculate_average(my_list)
print(f"Average: {result}")

my_empty_list = []
result = calculate_average(my_empty_list)
print(f"Average of empty list: {result}")

my_list_with_zero = [10, 0, 20, 30]
result = calculate_average(my_list_with_zero)
print(f"Average of list with zero: {result}")

my_list_with_strings = [10, 20, 'thirty', 40]
result = calculate_average(my_list_with_strings) 
print(f"Average of list with strings: {result}") #This will now return 0 instead of raising TypeError