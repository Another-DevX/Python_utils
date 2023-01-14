import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
    

def run():
    list_length = int(input("Put the list lenght"))
    searchingList = [random.randint(0,100) for i in range(list_length)]
    print(quicksort(searchingList))
    
if __name__ == "__main__":
    run()