import sys

def basic_operations(a,b):
    try:
        addition = a + b
        substraction = a - b
        multipication = a * b
        division = a / b
        return{"addition": addition, "substraction": substraction, "multipication": multipication, "division": division}
    except ZeroDivisionError:
        print("Error: division by zero")
        sys.exit(1)
def power_operations(base, exponent, **kwargs):
    try:
        result = base ** exponent
        if 'modulo' in kwargs:
            result %= kwargs['modulo']
            return result
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
def apply_operations(operation_list):
    try:
        return list(map(lambda x: x[0](*x[1]), operation_list))
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)