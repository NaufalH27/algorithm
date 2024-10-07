testCase1 = [2, 3, 20, 4, 6, 2, 1, 4, 693, 31, 4, 4]
testCase2 = [2, 3, 20, 4, 6, 2, 1, 4, 693, 31, 4]



def mergeSort(array : list) -> list :
    arraySize : int = len(array)
    if arraySize == 1:
        return array
    
    mid : int = arraySize // 2
    halfLeft : list = array[0 : mid]
    halfRight : list = array[mid : arraySize]
    left : list = mergeSort(halfLeft)
    right : list = mergeSort(halfRight)
        
    return combine(left,right)


def combine(left : list, right : list) -> list :
    leftPointer = 0
    rightPointer = 0
    mergedArray = []
    while(leftPointer < len(left) and rightPointer < len(right)):
        currLeft = left[leftPointer]
        currRight = right[rightPointer]
        if currLeft < currRight:
            mergedArray.append(currLeft)
            leftPointer += 1

        elif currLeft > currRight:
            mergedArray.append(currRight)
            rightPointer += 1
        
        else: 
            mergedArray.append(currLeft)
            mergedArray.append(currRight)
            leftPointer += 1
            rightPointer += 1
        
    return mergedArray + left[leftPointer:] + right[rightPointer:]


print(mergeSort(testCase1))
print(mergeSort(testCase2))