import random

#This script is an example of a O(n) complexity algoritm, sequential
    
def linear(searchingList, objetive):
    match = False
    
    for element in searchingList:
        if element == objetive:
            match = True
            return match

def run():
    objetive = int(input("Put the objetive"))
    list_length = int(input("Put the list lenght"))
    
    searchingList =[random.randint(0,100) for i in range(list_length)]
    match = linear(searchingList,objetive)
    print(searchingList)
    print(f'The element {objetive} {"Is in the list "if match == True else "Is not in the list"}') 
    
if __name__ == "__main__":
    run()