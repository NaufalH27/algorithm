testCase1 = [2, 3, 4, 4, 6, 2, 4, 4, 693, 31, 10, 20]
testCase2 = [2, 3, 20, 4, 6, 20, 10, 4, 693, 31, 4]
testCase3 = [3, 2, 8, 1, 5]

def partition(array : list) -> list :
    arraySize = len(array)
    pivot = 0
    left = 0
    right = arraySize - 1
    print(array[pivot])
    
    while left <= right :
        while array[left] < array[pivot]:
            left += 1
        while array[right] > array[pivot]:
            right -= 1

        if left <= right:
            array[left], array[right] = array[right], array[left]
        
        
        left += 1
        right -= 1
    
    return array


print(quicksort(testCase1))
print(quicksort(testCase2))
print(quicksort(testCase3))