from recursive.factorial_recursive import run_get_factorial as factorial
from recursive.fibonacci_recursive import run_fibonnaci_recursive as fibonacci



if __name__ ==  '__main__':

    response = int(input(
        """
Select a program 
--get_factorial__1 
--get_fibonacci_sequence__2 
        """
        ))
    try:
        response == 1 or response == 2
    except:
        raise Exception("Put a correct answer")
    
    if response == 1:
        value = int(input("select a number to search factorial"))
        factorial(value)
    elif response == 2:
        value = int(input("select fibonacci position"))
        fibonacci(value)