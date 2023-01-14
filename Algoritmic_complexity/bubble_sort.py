import random

#Quadratic growth, is'nt efficient

def buble(sortList):
    length = len(sortList)
    for i in range(length):
        for j in range(0, length - i - 1): #O(n) * O(n) = 0(n**2)
            if sortList[j] > sortList[j + 1]:
                sortList[j], sortList[j + 1] = sortList[j+1], sortList[j]
    return sortList


def run():
    list_length = int(input("Put the list lenght"))
    searchingList = [random.randint(0,100) for i in range(list_length)]
    print(buble(searchingList))
    
if __name__ == "__main__":
    run()