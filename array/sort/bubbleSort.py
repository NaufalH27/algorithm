testCase = [2, 3, 20, 4, 6, 2, 1, 4, 693, 31, 4, 4]

def bubbleSort(array : list):
    arraySize = len(array)
    
    for i in range(arraySize):
        for j in range(0, arraySize-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    
    return array


print(bubbleSort(testCase))