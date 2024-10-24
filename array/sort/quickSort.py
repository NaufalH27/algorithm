testCase2 = [40,3,2,14,15,39,10,4,32,1,5,9,8,23,49,7,9,25] 


def partition(array, leftPtr, rightPtr) -> int:
    print(array)
    print("")
    pivot = array[leftPtr] 
    low = leftPtr + 1
    high = rightPtr

    while True:
        while low <= high and array[high] >= pivot:
            high -= 1
        while low <= high and array[low] <= pivot:
            low += 1
        
        if low <= high:
            array[low], array[high] = array[high], array[low] 
        else:
            break

    array[leftPtr], array[high] = array[high], array[leftPtr] 
    return high  

def quick_sort(array, left, right):

    if left < right:
        j = partition(array,left, right)
        quick_sort(array, left, j-1)
        quick_sort(array, j+1, right)
    
    return array


print(quick_sort(testCase2,0, len(testCase2) -1))