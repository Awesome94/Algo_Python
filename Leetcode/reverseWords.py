def reverseWords(s: str) -> str:
    x = s.split(" ")
    for i in range(len(x)):
        x[i] = x[i][::-1]
    return ' '.join(x)

print(reverseWords("Let's take LeetCode contest"))