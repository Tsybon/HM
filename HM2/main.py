def is_palindrome(item):

    item_str = str(item).lower()

    return item_str == item_str[::-1]


# print(is_palindrome("Anna"))
# print(is_palindrome("test"))
# print(is_palindrome(112233))
# print(is_palindrome(12321))

def simple_calculator(operation, a, b):
    try:
        # Check if a or b are numbers
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both a and b must be numbers")

        # Perform the operation
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/':
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return a / b
        else:
            raise ValueError("Unsupported operation")

    except TypeError as e:
        return f"Error: {e}"
    except ZeroDivisionError as e:
        return f"Error: {e}"
    except ValueError as e:
        return f"Error: {e}"

# print(simple_calculator('+', 5,3))
# print(simple_calculator('-', 5,3))
# print(simple_calculator('*', 5,3))
# print(simple_calculator('/', 10,0))
