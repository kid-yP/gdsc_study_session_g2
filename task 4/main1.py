from math_operations import basic_operations, power_operations, apply_operations

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("enter the amount of modulo:"))
result_basic = basic_operations(a, b)
print("Basic operations result:", result_basic)

result_power = power_operations(a, b)
print("Power Operation Result:", result_power)

result_power_modulo = power_operations(a, b, modulo = c)
print("Power Operation Result with modulo:", result_power_modulo)

operations = [
    (lambda x, y: x + y, (a, b)),
     (lambda x, y: x * y, (a, b))
]

result_apply = apply_operations(operations)
print("Apply operations result:", result_apply)