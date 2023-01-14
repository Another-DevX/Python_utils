import random


def lineal(searchingList, objetive):
    match = False
    lineal_steps = 0    
    for element in searchingList:
        lineal_steps += 1
        if element == objetive:
            match = True
            print(f"Linear research need: {lineal_steps} steps")
            return match

binary_steps = 0
def binary(researchList, start, end, objetive):
    global binary_steps
    binary_steps += 1
    if start > end:
        return False
    
    middle = (start + end) // 2
    
    if researchList[middle] == objetive:
        print(f"binary_research need {binary_steps} steps")
        return True
    elif researchList[middle] > objetive:
        return binary(researchList, start, middle - 1, objetive)
    else:
        return binary(researchList, middle, end, objetive)
    
    
def run():
    objetive = int(input("Put the objetive"))
    list_length = int(input("Put the list lenght"))

    searchingList =[random.randint(0,100) for i in range(list_length)]
    match = lineal(searchingList,objetive)
    binary(sorted(searchingList),0, len(searchingList), objetive)
    print(f'The element {objetive} {"Is in the list "if match == True else "Is not in the list"}')
    
if __name__ == "__main__":
    run()