def find_string_anagrans(str, pattern):
    n = len(str)
    result = []
    end = len(pattern)
    for i in range(n-end+1):
        current = str[i:i+end]
        if sorted(current) == sorted(pattern):
            result.append(i)
    return result

# print(find_string_anagrans("abbcabc", "abc"))

def find_string_anagrams(str, pattern):
    start, matched = 0, 0
    n = len(str)
    char_freq = {}
    result = []

    for char in pattern:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1

    for i in range(n):
        right_val = str[i]
        
        if right_val in char_freq:
            char_freq[right_val] -= 1
            if char_freq[right_val] == 0:
                matched += 1

        if matched == len(char_freq):
            result.append(start)

        if i >= len(pattern)-1:
            left_val = str[start]
            start+=1
            if left_val in char_freq:
                if char_freq[left_val]== 0:
                    matched -= 1
                char_freq[left_val] += 1

    return result

print(find_string_anagrams("abbcabc", "abc"))