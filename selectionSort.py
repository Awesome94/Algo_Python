def selection(array):
    """
    selection sort finds min index and swaps the numbers in the array accordingly
    """
    for x in range(len(array)):
        min_index  = x
        if array[min_index] > array[x]:
            min_index = x
            
            array[min_index], array[x] = array[x], array[min_index] 
    return array

array = [1, 12, 4, 21, 8, 42, 121]
print(selection(array))