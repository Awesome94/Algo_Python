def longest_palindrome(s):
    n = len(s)
    if n <= 1:
        return s
    if s == s[::-1]:
        return s
    longest_palindrome = s[0]

    for x in range(n):
        L = x-1
        R = x+1
        while L >= 0 and R < n:
            if s[L] == s[R]:
                new_palindrome = s[L:R+1]
                longest_palindrome = new_palindrome if len(new_palindrome) > len(
                    longest_palindrome) else longest_palindrome
                L -= 1
                R += 1
                continue
            else:
                break
    for j in range(n):
        x = j+1
        L = j-1
        R = x+1
        while x < n:
            if s[x] == s[j]:
                new_palindrome = s[j: x+1]
                longest_palindrome = new_palindrome if len(new_palindrome) > len(
                longest_palindrome) else longest_palindrome
                if R < n:
                    if s[L] == s[R]:
                        new_palindrome = s[L: R+1]
                        L-=1
                        R+=1
                        longest_palindrome = new_palindrome if len(new_palindrome) > len(
                        longest_palindrome) else longest_palindrome
                        continue
                x+=1
                continue
            else:
                break
    return longest_palindrome

print(longest_palindrome("22202022"))
print(longest_palindrome("bba"))
print(longest_palindrome("xaabbcccbbaax"))
print(longest_palindrome("babaddtattarrattatddetartrateedredividerb"))
print(longest_palindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
# "ddtattarrattatdd"
"etartrate"
