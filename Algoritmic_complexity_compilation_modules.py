from Algoritmic_complexity import lineal_research

import random

if __name__ ==  '__main__':

    def response_input():
        response = int(input(f'Select a program \n--lineal_research__1 \n--binary_research__2 '))
        try:
            assert response == 1 or response == 2, "the response is'nt 1 or 2"
            run(response)
        except AssertionError as e:
            print(e)
            print("Put a valid value")
            response_input()

    def run(response): 
        if response == 1:
            lineal_research.run()
        elif response == 2:
            pass
    response_input()