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

import time

def retry(func):
    def wrapper(*args, **kwargs):
        attempts = 0
        while attempts < 3:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                attempts += 1
                print(f"Attempt {attempts} failed with error: {e}")
                if attempts == 3:
                    print("Max retries reached. Function failed.")
                    raise e
                time.sleep(1)  # Adding a short delay before retrying
    return wrapper

@retry
def example(threshold):
    from random import random
    if random() <= threshold:
        raise Exception("Random failure")
    print("Function succeeded")

# example(0.9) # fail in 9 out of 10 cases
# example(0.5) # fail in 5 out of 10 cases
