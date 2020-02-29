# def reverseWords(s: str) -> str:
#     return " ".join(reversed(s.split()))


def reverseWords(s: str) -> str:
    s_list = s.split()
    i = 0
    j = len(s_list)-1

    while i < j:
        s_list[i], s_list[j] = s_list[j], s_list[i]
        i += 1
        j -= 1

    return " ".join(s_list)


print(reverseWords("  world!   hello  "))
