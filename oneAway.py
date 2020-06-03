def oneAway(strA, strB):
    char_freq = {}
    edit = 0
    for char in strA:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1
    for s in strB:
        if s in char_freq and char_freq[s] > 0:
            char_freq[s] -= 1
        else:
            edit+=1
    return edit+sum(list(char_freq.values())) <= 1

print(oneAway("bake", "ble"))