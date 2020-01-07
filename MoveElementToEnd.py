def moveElementToEnd(array, toMove):
    i = 0
    len_array = len(array)-1
    while i < len_array:
        while len_array > i and array[len_array] == toMove:
            len_array-=1
        if array[i] == toMove:
            array[i], array[len_array] = array[len_array], array[i]
            len_array-=1
            i+=1
        i+=1
    return array

arr =  [2, 1, 2, 2, 2, 3, 4, 2]
num = 2
print(moveElementToEnd(arr, num))
