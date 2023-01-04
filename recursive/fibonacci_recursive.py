def fibonacci(amount):
    """fibonacci_recursive

    Args:
        amount (INT): an positive integer number

    Returns:
        fibonacci_number: returns a fibonnaci number in the amount position
    """
    if amount == 0 or amount == 1:
        return 1
    return fibonacci(amount - 1) + fibonacci(amount - 2)

def run_fibonnaci_recursive(value):
    for iterator in range(value):
        amount = iterator
        print(fibonacci(amount))

if __name__ ==  '__main__':
    run_fibonnaci_recursive(10)