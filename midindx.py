def solve(s):
    print("this is it")
    count_h = 0
    count_l = 0
    if len(s) < 10:
        return False
    for x in range(0, len(s), 5):
        if s[x-5:x] == "hippo":
            count_h += 1
    for x in range(0, len(s), 5):
        if s[x-5:x] == "llama":
            count_l += 1
    print(count_h, count_l)

solve("hippollamahippohelloworldllama")
