def stringRotation(string1, string2):
    n = len(string1)
    indx = 0
    if n != len(string2): return False
    for i in range(n):
        if string2.count(string1) == 1:
            break
        indx+=1
    return string1[:indx]+string2[:-indx] == string1

# print(stringRotation("waterbottle", "erbottlewat"))


def areRotations(string1, string2): 
    size1 = len(string1) 
    size2 = len(string2) 
    temp = '' 

    if size1 != size2: 
        return 0

    temp = string1 + string1 
    print(temp, string2, temp.count(string2))
    if (temp.count(string2)> 0):
        return 1
    else: 
        return 0

# Driver program to test the above function 
string1 = "ACCD"
string2 = "ACDA"

if areRotations(string1, string2): 
    print("Strings are rotations of each other")
else: 
    print("Strings are not rotations of each other")

# This code is contributed by Bhavya Jain 
