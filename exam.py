def exam(v):
    wrongAns = v.count(0)
    correctAns = v.count(1)-wrongAns
    numOfQtns = 0
    n = len(v)
    x = 0
    if correctAns < 0:
        return 0
    if correctAns == wrongAns:
        return 1
    while x < n and correctAns >= numOfQtns:
        if v[x] == 1:
            correctAns -= 1
            numOfQtns += 1
        else:
            numOfQtns -= 1
            correctAns += 1
        x += 1
    return x


v = [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1,
     1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(exam(v))
