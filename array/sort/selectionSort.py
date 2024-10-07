testCase = [2, 3, 20, 4, 6, 2, 1, 4, 693, 31, 4, 4]

def selectionSort(array : list) -> list:
    arraySize = len(array)
    
    for i in range(arraySize):
        
        smallest = i
        for j in range(i+1, arraySize):
            if array[j] < array[smallest]:
                smallest =j
            
                
        if smallest != i:
            array[i], array[smallest] =  array[smallest],  array[i]
    
    return array


print(selectionSort(testCase))