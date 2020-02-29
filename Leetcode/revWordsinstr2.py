def reverseWords(s) -> list:
    s[:] = list(' '.join(''.join(s).split()[::-1]))
    return s


print(reverseWords(["t", "h", "e", " ", "s", "k",
                    "y", " ", "i", "s", " ", "b", "l", "u", "e"]))
