def find_common_char(arr1, arr2):
    return [x for x in arr1 if x in arr2]

def find_common_char_sets(arr1, arr2):
    return set(arr1).symmetric_difference(set(arr2)).union()
arr1 = [22,13,12,2,1,54]
arr2 = [12,2,1,231,212,1]
print(find_common_char_sets(arr1, arr2))
