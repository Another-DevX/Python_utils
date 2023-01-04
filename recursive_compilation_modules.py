from recursive.factorial_recursive import run_get_factorial as factorial
from recursive.fibonacci_recursive import run_fibonnaci_recursive as fibonacci



if __name__ ==  '__main__':

    def response_input():
        response = int(input(f'Select a program \n--get_factorial__1 \n--get_fibonacci_sequence__2 '))
        try:
            assert response == 1 or response == 2
            run(response)
        except AssertionError as e:
            print(e)
            print("Escribe un valor valido")
            response_input()

    def run(response): 
        if response == 1:
            value = int(input("select a number to search factorial"))
            factorial(value)
        elif response == 2:
            value = int(input("select fibonacci position"))
            fibonacci(value)
    response_input()