import random

#Quadratic growth, is'nt efficient

def insertion(sortList):
    for i in range (1,len(sortList)):
        value = sortList[i]
        index = i
        while index > 0 and sortList[index - 1] > value:
            sortList[index] = sortList[index - 1]
            index -= 1
        sortList[index] = value
    return sortList

def run():
    list_length = int(input("Put the list lenght"))
    searchingList = [random.randint(0,100) for i in range(list_length)]
    print(insertion(searchingList))
    
if __name__ == "__main__":
    run()