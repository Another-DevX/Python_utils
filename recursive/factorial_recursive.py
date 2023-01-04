def get_factorial(value):
    """get_factorial_result

    Args:
        value (INT): A positive integer number

    Returns:
        Value!: get the result of value Factorial like (n! = n * (n -1)!)
    """
    if value == 1:
        return 1
    return value * get_factorial(value - 1)
        

def run_get_factorial(value):
    print(get_factorial(value))
        

if __name__ ==  '__main__':
    run_get_factorial(5)