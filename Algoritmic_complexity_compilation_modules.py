from Algoritmic_complexity import lineal_research, binary_research, comparasion,bubble_sort,insertion_sort, merge_sort,merge_sort_compact

import random

if __name__ ==  '__main__':

    def response_input():
        response = int(input(f'Select a program \n--lineal_research__1 \n--binary_research__2 \n--comparasion__3 \n--bubble_sort__4 \n--insertion_sort__5 \n--merge-sort__6 \n --merge_sort_compact__7'))
        try:
            assert response in (1,7)  , "the response is'nt in 1 to 7"
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
        elif response == 6:
            merge_sort,run()
        elif response == 7:     
            merge_sort_compact,run()
    response_input()