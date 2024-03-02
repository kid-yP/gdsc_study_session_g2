n = int(input ("enter the value of n: "))
def even_or_odd(m):
    if m % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_or_odd(n)

num1 = int(input ("enter the first value: "))
num2 = int(input ("enter the second value: "))
def find_maximum(a, b):
    return max(a, b)
result = find_maximum(num1, num2)
print(f"The maximum of {num1} and {num2} is: {result}")

year = int(input ("enter the the year: "))
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap Year"
    else:
        return "Not a Leap Year"
input_year = year
result = is_leap_year(input_year)
print(f"{input_year} is {result}")

word = str(input("enter the string: "))
def check_string_length(input_string):
    if len(input_string) > 10:
        return "Long"
    else:
        return "Short"

user_input = word
result = check_string_length(user_input)
print(f"The input string is {result}")
"""
"""
def get_user_list():
    user_input = input("Enter a list of numbers separated by spaces: ")
    
    input_list = user_input.split()
    number_list = [int(num) for num in input_list]

    return number_list

user_list = get_user_list()
print("User input list:", user_list)


def sum_positive_numbers(numbers):
    return sum(num for num in numbers if num > 0)

number_list = user_list
result = sum_positive_numbers(number_list)
print(f"The sum of positive numbers in the list is: {result}")


def print_numbers_up_to_n(n):
    for i in range(1, n + 1):
       print(i)
        
user_input = int(input("Enter a value for n: "))
print_numbers_up_to_n(user_input)







