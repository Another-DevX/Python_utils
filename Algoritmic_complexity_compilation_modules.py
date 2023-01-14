from Algoritmic_complexity import lineal_research, binary_research, comparasion,bubble_sort,insertion_sort

import random

if __name__ ==  '__main__':

    def response_input():
        response = int(input(f'Select a program \n--lineal_research__1 \n--binary_research__2 \n--comparasion__3 \n--bubble_sort__4 \n--insertion_sort__5'))
        try:
            assert response in (1,5)  , "the response is'nt in 1 to 5"
            run(response)
        except AssertionError as e:
            print(e)
            print("Put a valid value")
            response_input()

    def run(response): 
        if response == 1:
            lineal_research.run()
        elif response == 2:
            binary_research.run()
        elif response == 3:
            comparasion.run()
        elif response == 4:
            bubble_sort.run()
        elif response == 5:
            insertion_sort,run()
    response_input()