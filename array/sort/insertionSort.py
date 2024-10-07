testCase = [2, 3, 20, 4, 6, 2, 1, 4, 693, 31, 4, 4]

def insertionSort(array : list) -> list :
    arraySize : int = len(array)

    for i in range(arraySize):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    
    return array  
         
         
print(insertionSort(testCase))   




