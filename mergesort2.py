def merge(arr):
    mid = len(arr)//2
    if len(arr) > 1:
        arr1 = arr[mid:]
        arr2 = arr[:mid]
        merge(arr1)
        merge(arr2)

        i=j=k=0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                arr[k] = arr1[i]
                i+=1   
            else:
                arr[k] = arr2[j]
                j+=1
            k+=1
        while i < len(arr1):
            arr[k] = arr1[i]
            k+=1
            i+=1
        while j < len(arr2):
            arr[k] = arr2[j]
            k+=1
            j+=1
    return arr

print(merge([12,1,3,1,121,10,21]))
