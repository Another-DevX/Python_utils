import random

#This script is a example for a O(log n) complexity algoritm, logaritm

def binary(researchList, start, end, objetive):

    if start > end:
        return False
    
    middle = (start + end) // 2
    
    if researchList[middle] == objetive:
        return True
    elif researchList[middle] > objetive:
        return binary(researchList, start, middle - 1, objetive)
    else:
        return binary(researchList, middle, end, objetive)
    
    
def run():
    objetive = int(input("Put te objetive"))
    list_length = int(input("Put the list lenght"))

    searchingList =sorted([random.randint(0,100) for i in range(list_length)])
    match = binary(searchingList,0, len(searchingList), objetive)
    print(searchingList)
    print(f'The element {objetive} {"Is in the list "if match == True else "Is not in the list"}')
    
if __name__ == "__main__":
    run()