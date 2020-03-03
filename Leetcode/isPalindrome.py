def isPalindrome(s):
    new_str = ""
    reversed_str = ""
    for x in s:
        if x.isalpha() or x.isdigit():
            new_str += x.lower()

    for i in range(len(new_str)-1, -1, -1):
        reversed_str += new_str[i]

    return new_str == reversed_str


print(isPalindrome("0P"))

# A man, a plan, a canal: Panama
