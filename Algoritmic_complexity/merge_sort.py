import random

#Logaritmical, very efficent

def merge(sortList):
    if len(sortList) > 1:
        middle =  len(sortList) // 2
        left = sortList[:middle]
        right = sortList[middle:]
        #Recursive call in each sublist
        merge(left)
        merge(right)
        
        #Iterators
        i = 0
        j = 0
        k = 0 
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sortList[k] = left[i]
                i += 1
            else:
                sortList[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            sortList[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            sortList[k] = right[j]
            j += 1
            k += 1  
    return sortList   
    pass

def run():
    list_length = int(input("Put the list lenght"))
    searchingList = [random.randint(0,100) for i in range(list_length)]
    print(merge(searchingList))
    
if __name__ == "__main__":
    run()